from pytm import TM, Actor, Boundary, Dataflow, Datastore, Process, Classification 
  
tm = TM("HOS05A Stateful Session Threat Model") 
tm.description = "Threat model for the HOS05A question_answering_agent with InMemorySessionService." 
tm.isOrdered = True 
tm.mergeResponses = True 
  
internet = Boundary("Internet") 
gcp_boundary = Boundary("Google Cloud Platform") 
server_boundary = Boundary("HOS05A Server") 
venv_boundary = Boundary("Python Virtual Environment (.venv)") 
session_boundary = Boundary("InMemorySessionService (Session State)")   # NEW 
  
user = Actor("User (Terminal)") 
user.inBoundary = internet 
  
google_llm = Actor("Google Gemini API") 
google_llm.inBoundary = gcp_boundary 
  
main_script = Process("basic_stateful_session.py") 
main_script.inBoundary = server_boundary 
main_script.sanitizesInput = False 
  
runner_process = Process("Runner (ADK)") 
runner_process.inBoundary = venv_boundary 
  
question_agent = Process("question_answering_agent") 
question_agent.inBoundary = venv_boundary 
question_agent.sanitizesInput = False 
  
placeholder_injector = Process("Placeholder Injector ({user_name}, {user_preferences})")   # NEW 
placeholder_injector.inBoundary = session_boundary 
placeholder_injector.sanitizesInput = False 
  
env_file = Datastore(".env File") 
env_file.inBoundary = server_boundary 
env_file.isEncrypted = False 
env_file.storesSensitiveData = True 
env_file.classification = Classification.SECRET 
  
session_state_store = Datastore("InMemorySessionService (user_name, user_preferences)")   # NEW 
session_state_store.inBoundary = session_boundary 
session_state_store.isEncrypted = False 
session_state_store.storesSensitiveData = True 
session_state_store.classification = Classification.SENSITIVE 
  
user_to_script = Dataflow(user, main_script, "User Query (terminal input)") 
user_to_script.sanitizes = False 
  
env_to_script = Dataflow(env_file, main_script, "API Key + Config") 
env_to_script.isEncrypted = False 
env_to_script.classification = Classification.SECRET 
  
init_to_store = Dataflow(main_script, session_state_store,   # NEW 
    "Initial State (user_name, user_preferences)") 
init_to_store.classification = Classification.SENSITIVE 
  
store_to_runner = Dataflow(session_state_store, runner_process,   # NEW 
    "Session State for Prompt Injection") 
store_to_runner.sanitizes = False 
  
runner_to_injector = Dataflow(runner_process, placeholder_injector,   # NEW 
    "Template Prompt + State Values") 
runner_to_injector.sanitizes = False 
  
injector_to_agent = Dataflow(placeholder_injector, question_agent,   # NEW 
    "Personalized Prompt (state injected into {user_name}, {user_preferences})") 
injector_to_agent.sanitizes = False 
  
agent_to_llm = Dataflow(question_agent, google_llm, "API Request + Personalized Prompt (HTTPS)") 
agent_to_llm.protocol = "HTTPS" 
agent_to_llm.isEncrypted = True 
agent_to_llm.classification = Classification.SENSITIVE 
  
llm_to_agent = Dataflow(google_llm, question_agent, "LLM Response (HTTPS)") 
llm_to_agent.protocol = "HTTPS" 
llm_to_agent.isEncrypted = True 
  
runner_to_store = Dataflow(runner_process, session_state_store,   # NEW 
    "Updated Session State (after agent response)") 
runner_to_store.classification = Classification.SENSITIVE 
  
agent_to_user = Dataflow(main_script, user, "Final Response (terminal output)") 
  
if __name__ == "__main__": 
    tm.process()