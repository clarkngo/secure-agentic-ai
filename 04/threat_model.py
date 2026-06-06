from pytm import TM, Actor, Boundary, Dataflow, Datastore, Process, Classification 
  
tm = TM("HOS04A Email Agent Threat Model") 
tm.description = "Threat model for the HOS04A email_agent with Pydantic structured output." 
tm.isOrdered = True 
tm.mergeResponses = True 
  
internet = Boundary("Internet") 
gcp_boundary = Boundary("Google Cloud Platform") 
server_boundary = Boundary("HOS04A Server") 
venv_boundary = Boundary("Python Virtual Environment (.venv)") 
pydantic_boundary = Boundary("Pydantic Validation Layer")   # NEW 
  
user = Actor("Web Browser User") 
user.inBoundary = internet 
  
google_llm = Actor("Google Gemini API") 
google_llm.inBoundary = gcp_boundary 
  
adk_web_ui = Process("adk web (Dev UI)") 
adk_web_ui.inBoundary = server_boundary 
adk_web_ui.sanitizesInput = False 
  
agent_process = Process("agent.py (email_agent)") 
agent_process.inBoundary = venv_boundary 
agent_process.sanitizesInput = False 
agent_process.validatesInput = False 
  
pydantic_validator = Process("Pydantic Validator - EmailContent")   # FIXED 
pydantic_validator.inBoundary = pydantic_boundary 
pydantic_validator.sanitizesInput = False 
pydantic_validator.validatesInput = True   # Pydantic enforces schema validation 
  
env_file = Datastore(".env File") 
env_file.inBoundary = server_boundary 
env_file.isEncrypted = False 
env_file.storesSensitiveData = True 
env_file.classification = Classification.SECRET 
  
output_key_store = Datastore("output_key Store - email")   # FIXED 
output_key_store.inBoundary = venv_boundary 
output_key_store.isEncrypted = False 
output_key_store.storesSensitiveData = True 
output_key_store.classification = Classification.SENSITIVE 
  
user_to_ui = Dataflow(user, adk_web_ui, "User Email Request (HTTP)") 
user_to_ui.protocol = "HTTP" 
user_to_ui.isEncrypted = False 
user_to_ui.sanitizes = False 
  
ui_to_agent = Dataflow(adk_web_ui, agent_process, "Routed Prompt") 
ui_to_agent.sanitizes = False 
  
env_to_agent = Dataflow(env_file, agent_process, "API Key + Config") 
env_to_agent.isEncrypted = False 
env_to_agent.classification = Classification.SECRET 
  
agent_to_llm = Dataflow(agent_process, google_llm, 
    "API Request + EmailContent Schema (HTTPS)") 
agent_to_llm.protocol = "HTTPS" 
agent_to_llm.isEncrypted = True 
agent_to_llm.classification = Classification.SENSITIVE 
  
llm_to_agent = Dataflow(google_llm, agent_process, "JSON Response (HTTPS)") 
llm_to_agent.protocol = "HTTPS" 
llm_to_agent.isEncrypted = True 
  
agent_to_pydantic = Dataflow(agent_process, pydantic_validator,   # NEW 
    "Raw JSON for Validation") 
agent_to_pydantic.sanitizes = False 
  
pydantic_to_store = Dataflow(pydantic_validator, output_key_store,   # NEW 
    "Validated EmailContent") 
  
store_to_agent = Dataflow(output_key_store, agent_process,   # FIXED 
    "Validated Output email") 
  
agent_to_ui = Dataflow(agent_process, adk_web_ui, "Structured Email Response") 
agent_to_ui.sanitizes = False 
  
ui_to_user = Dataflow(adk_web_ui, user, "Response (HTTP)") 
ui_to_user.isEncrypted = False 
  
if __name__ == "__main__": 
    tm.process()