from pytm import TM, Actor, Boundary, Dataflow, Datastore, Process, Classification 
  
tm = TM("HOS06A Memory Agent Threat Model") 
tm.description = "Threat model for the HOS06A memory_agent with DatabaseSessionService and SQLite." 
tm.isOrdered = True 
tm.mergeResponses = True 
  
internet = Boundary("Internet") 
gcp_boundary = Boundary("Google Cloud Platform") 
server_boundary = Boundary("HOS06A Server") 
venv_boundary = Boundary("Python Virtual Environment (.venv)") 
tool_boundary = Boundary("Tool Execution Layer (ToolContext)") 
sqlite_boundary = Boundary("SQLite Persistent Storage")   # NEW 
  
user = Actor("User (CLI Terminal)") 
user.inBoundary = internet 
  
google_llm = Actor("Google Gemini API") 
google_llm.inBoundary = gcp_boundary 
  
main_process = Process("main.py") 
main_process.inBoundary = server_boundary 
main_process.sanitizesInput = False 
  
runner_process = Process("Runner (ADK)") 
runner_process.inBoundary = venv_boundary 
  
memory_agent_proc = Process("memory_agent") 
memory_agent_proc.inBoundary = venv_boundary 
memory_agent_proc.sanitizesInput = False 
memory_agent_proc.validatesInput = False 
  
tool_executor = Process("Tool Executor (add/view/update/delete/update_user_name)")   # NEW 
tool_executor.inBoundary = tool_boundary 
tool_executor.sanitizesInput = False 
  
env_file = Datastore(".env File") 
env_file.inBoundary = server_boundary 
env_file.isEncrypted = False 
env_file.storesSensitiveData = True 
env_file.classification = Classification.SECRET 
  
sqlite_db = Datastore("my_agent_data.db (SQLite)")   # NEW 
sqlite_db.inBoundary = sqlite_boundary 
sqlite_db.isEncrypted = False 
sqlite_db.storesSensitiveData = True 
sqlite_db.classification = Classification.SENSITIVE 
  
user_to_main = Dataflow(user, main_process, "User CLI Input") 
user_to_main.sanitizes = False 
  
env_to_main = Dataflow(env_file, main_process, "API Key + Config") 
env_to_main.isEncrypted = False 
env_to_main.classification = Classification.SECRET 
  
main_to_sqlite = Dataflow(main_process, sqlite_db,   # NEW 
    "DatabaseSessionService (create/retrieve session)") 
main_to_sqlite.isEncrypted = False 
  
sqlite_to_main = Dataflow(sqlite_db, main_process,   # NEW 
    "Existing Session Data (user_name, reminders)") 
sqlite_to_main.classification = Classification.SENSITIVE 
  
agent_to_llm = Dataflow(memory_agent_proc, google_llm, "API Request + Tool Definitions (HTTPS)") 
agent_to_llm.protocol = "HTTPS" 
agent_to_llm.isEncrypted = True 
agent_to_llm.classification = Classification.SENSITIVE 
  
llm_to_agent = Dataflow(google_llm, memory_agent_proc, "LLM Response / Tool Call Request (HTTPS)") 
llm_to_agent.protocol = "HTTPS" 
llm_to_agent.isEncrypted = True 
  
agent_to_tools = Dataflow(memory_agent_proc, tool_executor,   # NEW 
    "Tool Call (e.g., add_reminder, delete_reminder)") 
agent_to_tools.sanitizes = False 
  
tools_to_sqlite = Dataflow(tool_executor, sqlite_db,   # NEW 
    "State Update via ToolContext (user_name, reminders)") 
tools_to_sqlite.isEncrypted = False 
  
sqlite_to_tools = Dataflow(sqlite_db, tool_executor,   # NEW 
    "Current State Read via ToolContext") 
sqlite_to_tools.classification = Classification.SENSITIVE 
  
if __name__ == "__main__": 
    tm.process()