from pytm import TM, Actor, Boundary, Dataflow, Datastore, Process, Classification 
  
tm = TM("HOS07A Manager MAS Threat Model") 
tm.description = "Threat model for the HOS07A manager multi-agent system." 
tm.isOrdered = True 
tm.mergeResponses = True 
  
internet = Boundary("Internet") 
gcp_boundary = Boundary("Google Cloud Platform") 
server_boundary = Boundary("HOS07A Server") 
venv_boundary = Boundary("Python Virtual Environment (.venv)") 
stock_boundary = Boundary("Stock Analyst Agent Boundary")   # NEW 
funny_boundary = Boundary("Funny Nerd Agent Boundary")   # NEW 
news_boundary = Boundary("News Analyst AgentTool Boundary")   # NEW 
yahoo_boundary = Boundary("Yahoo Finance (External Market Data)")   # NEW 
  
user = Actor("Web Browser User") 
user.inBoundary = internet 
  
google_llm = Actor("Google Gemini API") 
google_llm.inBoundary = gcp_boundary 
  
yahoo_finance = Actor("Yahoo Finance API (yfinance)")   # NEW 
yahoo_finance.inBoundary = yahoo_boundary 
  
adk_web_ui = Process("adk web (Dev UI)") 
adk_web_ui.inBoundary = server_boundary 
adk_web_ui.sanitizesInput = False 
  
manager_agent = Process("manager (root_agent)") 
manager_agent.inBoundary = venv_boundary 
manager_agent.sanitizesInput = False 
manager_agent.validatesInput = False 
  
stock_analyst = Process("stock_analyst (sub-agent, delegation)")   # NEW 
stock_analyst.inBoundary = stock_boundary 
stock_analyst.sanitizesInput = False 
  
funny_nerd = Process("funny_nerd (sub-agent, delegation)")   # NEW 
funny_nerd.inBoundary = funny_boundary 
funny_nerd.sanitizesInput = False 
  
news_analyst = Process("news_analyst (AgentTool, agent-as-tool)")   # NEW 
news_analyst.inBoundary = news_boundary 
news_analyst.sanitizesInput = False 
  
get_current_time_func = Process("get_current_time (tool)") 
get_current_time_func.inBoundary = venv_boundary 
  
env_file = Datastore("manager/.env File") 
env_file.inBoundary = server_boundary 
env_file.isEncrypted = False 
env_file.storesSensitiveData = True 
env_file.classification = Classification.SECRET 
  
user_to_ui = Dataflow(user, adk_web_ui, "User Prompt (HTTP)") 
user_to_ui.protocol = "HTTP" 
user_to_ui.isEncrypted = False 
user_to_ui.sanitizes = False 
  
env_to_manager = Dataflow(env_file, manager_agent, "API Key + Config") 
env_to_manager.isEncrypted = False 
env_to_manager.classification = Classification.SECRET 
  
manager_to_llm = Dataflow(manager_agent, google_llm, "Delegation Request + Prompt (HTTPS)") 
manager_to_llm.protocol = "HTTPS" 
manager_to_llm.isEncrypted = True 
manager_to_llm.classification = Classification.SENSITIVE 
  
llm_to_manager = Dataflow(google_llm, manager_agent, "Delegation Decision / Response (HTTPS)") 
llm_to_manager.protocol = "HTTPS" 
llm_to_manager.isEncrypted = True 
  
manager_to_stock = Dataflow(manager_agent, stock_analyst,   # NEW 
    "Delegated Financial Query (sub-agent delegation)") 
manager_to_stock.sanitizes = False 
  
stock_to_yahoo = Dataflow(stock_analyst, yahoo_finance,   # NEW 
    "Stock Data Request (yfinance, HTTPS)") 
stock_to_yahoo.protocol = "HTTPS" 
stock_to_yahoo.isEncrypted = True 
  
yahoo_to_stock = Dataflow(yahoo_finance, stock_analyst,   # NEW 
    "Market Data Response") 
yahoo_to_stock.sanitizes = False 
  
stock_to_manager = Dataflow(stock_analyst, manager_agent,   # NEW 
    "Financial Analysis Result") 
stock_to_manager.sanitizes = False 
  
manager_to_funny = Dataflow(manager_agent, funny_nerd,   # NEW 
    "Delegated Joke Request (sub-agent delegation)") 
manager_to_funny.sanitizes = False 
  
funny_to_manager = Dataflow(funny_nerd, manager_agent,   # NEW 
    "Joke Result") 
funny_to_manager.sanitizes = False 
  
manager_to_news = Dataflow(manager_agent, news_analyst,   # NEW 
    "AgentTool Call (synchronous)") 
manager_to_news.sanitizes = False 
  
news_to_manager = Dataflow(news_analyst, manager_agent,   # NEW 
    "News Analysis Result") 
news_to_manager.sanitizes = False 
  
manager_to_time = Dataflow(manager_agent, get_current_time_func, "get_current_time() call") 
  
time_to_manager = Dataflow(get_current_time_func, manager_agent, "Current Timestamp") 
  
ui_to_user = Dataflow(adk_web_ui, user, "Response (HTTP)") 
ui_to_user.isEncrypted = False 
  
if __name__ == "__main__": 
    tm.process()