from pytm import TM, Actor, Boundary, Dataflow, Datastore, Process, Classification 

tm = TM("HOS01A Greeting Agent Threat Model") 
tm.description = "Threat model for the HOS01A greeting agent." 
tm.isOrdered = True 
tm.mergeResponses = True 

internet = Boundary("Internet") 
gcp_boundary = Boundary("Google Cloud Platform") 
server_boundary = Boundary("HOS01A Server") 
venv_boundary = Boundary("Python Virtual Environment (.venv)") 

user = Actor("Web Browser User") 
user.inBoundary = internet 

google_llm = Actor("Google Gemini API") 
google_llm.inBoundary = gcp_boundary 

adk_web_ui = Process("adk web (Dev UI)") 
adk_web_ui.inBoundary = server_boundary 
adk_web_ui.sanitizesInput = False 

agent_process = Process("agent.py (greeting_agent)") 
agent_process.inBoundary = venv_boundary 
agent_process.sanitizesInput = False 
agent_process.validatesInput = False 

env_file = Datastore(".env File") 
env_file.inBoundary = server_boundary 
env_file.isEncrypted = False 
env_file.storesSensitiveData = True 
env_file.classification = Classification.SECRET 

user_to_ui = Dataflow(user, adk_web_ui, "User Prompt (HTTP)") 
user_to_ui.protocol = "HTTP" 
user_to_ui.isEncrypted = False 
user_to_ui.sanitizes = False 

ui_to_agent = Dataflow(adk_web_ui, agent_process, "Routed Prompt") 
ui_to_agent.sanitizes = False 

env_to_agent = Dataflow(env_file, agent_process, "API Key + Config") 
env_to_agent.isEncrypted = False 
env_to_agent.classification = Classification.SECRET 

agent_to_llm = Dataflow(agent_process, google_llm, "API Request (HTTPS)") 
agent_to_llm.protocol = "HTTPS" 
agent_to_llm.isEncrypted = True 
agent_to_llm.classification = Classification.SENSITIVE 

llm_to_agent = Dataflow(google_llm, agent_process, "LLM Response (HTTPS)") 
llm_to_agent.protocol = "HTTPS" 
llm_to_agent.isEncrypted = True 

ui_to_user = Dataflow(adk_web_ui, user, "Response (HTTP)") 
ui_to_user.isEncrypted = False 

if __name__ == "__main__": 
    tm.process()