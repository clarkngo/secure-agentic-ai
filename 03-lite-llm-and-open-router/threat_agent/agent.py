import os 
from google.adk.agents import Agent 
from google.adk.models.lite_llm import LiteLlm 
  
_REPORT_PATH = os.path.join(os.path.dirname(__file__), "..", "threats.md") 
  
def _load_report(path): 
    resolved = os.path.abspath(path) 
    if not os.path.exists(resolved): 
        return "Threat report not found. Run: python threat_model.py --report threats.md" 
    with open(resolved, "r", encoding="utf-8") as f: 
        return f.read() 
  
_report = _load_report(_REPORT_PATH) 
  
model = LiteLlm( 
    model="openrouter/openai/gpt-4.1", 
    api_key=os.getenv("OPENROUTER_API_KEY") 
) 
  
root_agent = Agent( 
    name="threat_modeling_agent", 
    model=model, 
    description="A security analyst agent that reviews threat models for tool-enabled AI agent systems.", 
    instruction=f""" 
You are an expert application security engineer and AI safety specialist. 
You have been given the following pytm-generated threat report for a tool-enabled AI agent: 
 
--- 
{_report} 
--- 
 
Your responsibilities: 
1. Answer questions about the threats clearly and accurately. 
2. Identify threats pytm may have missed, especially LLM-specific and tool-specific threats such as: 
   - Prompt Injection (LLM01): user input overriding system instructions or manipulating tool call arguments 
   - Sensitive Information Disclosure (LLM02): model or tools revealing sensitive data in responses 
   - Model Denial of Service (LLM04): adversarial prompts causing excessive or looping tool invocations 
   - Insecure Output Handling (LLM05): agent output or tool results rendered without sanitization 
   - Tool Misuse (ASI02): agent invoking tools with attacker-controlled arguments due to prompt injection 
   - Third-Party Gateway Risk: data sent via LiteLLM to OpenRouter traverses an external third-party 
     service with its own data retention, privacy, and availability policies 
3. Recommend specific, actionable mitigations using STRIDE categories. 
4. When asked to prioritize, use Risk = Likelihood x Impact. 
5. Keep responses concise but precise. Use bullet points for lists. 
6. If uncertain, say so rather than guessing. 
7. Ground all answers in the system described in the threat report. 
""", 
)