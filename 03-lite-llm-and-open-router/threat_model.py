from pytm import TM, Actor, Boundary, Dataflow, Datastore, Process, Classification 
  
tm = TM("HOS03A Dad Joke Agent Threat Model") 
tm.description = "Threat model for the HOS03A dad_joke_agent (LiteLLM + OpenRouter)." 
tm.isOrdered = True 
tm.mergeResponses = True 
  
internet = Boundary("Internet") 
openrouter_boundary = Boundary("OpenRouter / External LLM Providers")   # NEW 
server_boundary = Boundary("HOS03A Server") 
venv_boundary = Boundary("Python Virtual Environment (.venv)") 
tool_boundary = Boundary("Tool Execution Layer") 
litellm_boundary = Boundary("LiteLLM Routing Layer")   # NEW 
  
user = Actor("Web Browser User") 
user.inBoundary = internet 
  
openrouter_api = Actor("OpenRouter API")   # NEW (replaces Google Gemini API) 
openrouter_api.inBoundary = openrouter_boundary 
  
adk_web_ui = Process("adk web (Dev UI)") 
adk_web_ui.inBoundary = server_boundary 
adk_web_ui.sanitizesInput = False 
  
agent_process = Process("agent.py (dad_joke_agent)") 
agent_process.inBoundary = venv_boundary 
agent_process.sanitizesInput = False 
agent_process.validatesInput = False 
  
litellm_process = Process("LiteLLM (Routing Layer)")   # NEW 
litellm_process.inBoundary = litellm_boundary 
litellm_process.sanitizesInput = False 
  
get_joke_func = Process("get_dad_joke()")   # NEW 
get_joke_func.inBoundary = tool_boundary 
get_joke_func.sanitizesInput = False 
  
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
  
agent_to_litellm = Dataflow(agent_process, litellm_process, "Prompt + Tool Definitions")   # NEW 
agent_to_litellm.sanitizes = False 
  
litellm_to_openrouter = Dataflow(litellm_process, openrouter_api, 
    "API Request with Tool Definitions (HTTPS)")   # NEW 
litellm_to_openrouter.protocol = "HTTPS" 
litellm_to_openrouter.isEncrypted = True 
litellm_to_openrouter.classification = Classification.SENSITIVE 
  
openrouter_to_litellm = Dataflow(openrouter_api, litellm_process, 
    "LLM Response / Tool Call Request (HTTPS)")   # NEW 
openrouter_to_litellm.protocol = "HTTPS" 
openrouter_to_litellm.isEncrypted = True 
  
litellm_to_agent = Dataflow(litellm_process, agent_process, 
    "Routed LLM Response / Tool Call Request")   # NEW 
litellm_to_agent.sanitizes = False 
  
agent_to_joke = Dataflow(agent_process, get_joke_func, "Tool Call: get_dad_joke()") 
agent_to_joke.sanitizes = False 
  
joke_to_agent = Dataflow(get_joke_func, agent_process, "Tool Result: Dad Joke") 
joke_to_agent.sanitizes = False 
  
ui_to_user = Dataflow(adk_web_ui, user, "Response (HTTP)") 
ui_to_user.isEncrypted = False 
  
if __name__ == "__main__": 
    tm.process()
