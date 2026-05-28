from pytm import TM, Actor, Boundary, Dataflow, Datastore, Process, Classification 
  
tm = TM("HOS02A Multi-Tool Agent Threat Model") 
tm.description = "Threat model for the HOS02A multi_tool_agent (weather_time_agent)." 
tm.isOrdered = True 
tm.mergeResponses = True 
  
internet = Boundary("Internet") 
gcp_boundary = Boundary("Google Cloud Platform") 
server_boundary = Boundary("HOS02A Server") 
venv_boundary = Boundary("Python Virtual Environment (.venv)") 
tool_boundary = Boundary("Tool Execution Layer")   # NEW 
  
user = Actor("Web Browser User") 
user.inBoundary = internet 
  
google_llm = Actor("Google Gemini API") 
google_llm.inBoundary = gcp_boundary 
  
adk_web_ui = Process("adk web (Dev UI)") 
adk_web_ui.inBoundary = server_boundary 
adk_web_ui.sanitizesInput = False 
  
agent_process = Process("agent.py (weather_time_agent)") 
agent_process.inBoundary = venv_boundary 
agent_process.sanitizesInput = False 
agent_process.validatesInput = False 
  
get_weather_func = Process("get_weather(city)")   # NEW 
get_weather_func.inBoundary = tool_boundary 
get_weather_func.sanitizesInput = False 
  
get_time_func = Process("get_current_time(city)")  # NEW 
get_time_func.inBoundary = tool_boundary 
get_time_func.sanitizesInput = False 
  
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
  
agent_to_llm = Dataflow(agent_process, google_llm, "API Request with Tool Definitions (HTTPS)") 
agent_to_llm.protocol = "HTTPS" 
agent_to_llm.isEncrypted = True 
agent_to_llm.classification = Classification.SENSITIVE 
  
llm_to_agent = Dataflow(google_llm, agent_process, "LLM Response / Tool Call Request (HTTPS)") 
llm_to_agent.protocol = "HTTPS" 
llm_to_agent.isEncrypted = True 
  
agent_to_weather = Dataflow(agent_process, get_weather_func, "Tool Call: get_weather(city)") 
agent_to_weather.sanitizes = False 
  
weather_to_agent = Dataflow(get_weather_func, agent_process, "Tool Result: Weather Report") 
weather_to_agent.sanitizes = False 
  
agent_to_time = Dataflow(agent_process, get_time_func, "Tool Call: get_current_time(city)") 
agent_to_time.sanitizes = False 
  
time_to_agent = Dataflow(get_time_func, agent_process, "Tool Result: Current Time") 
time_to_agent.sanitizes = False 
  
ui_to_user = Dataflow(adk_web_ui, user, "Response (HTTP)") 
ui_to_user.isEncrypted = False 
  
if __name__ == "__main__": 
    tm.process()