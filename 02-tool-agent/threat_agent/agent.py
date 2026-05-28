import os
from google.adk.agents import Agent

_REPORT_PATH = os.path.join(os.path.dirname(__file__), "..", "threats.md")


def _load_report(path):
    resolved = os.path.abspath(path)
    if not os.path.exists(resolved):
        return "Threat report not found. Run: python threat_model.py --report threats.md"
    with open(resolved, "r", encoding="utf-8") as f:
        return f.read()


_report = _load_report(_REPORT_PATH)

root_agent = Agent(
    name="threat_modeling_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-3.5-flash",
    description="A security analyst agent that reviews threat models for AI agent systems.",
    instruction=f"""You are an expert application security engineer and AI safety specialist.
You have been given the following pytm-generated threat report:

---
{_report}
---

Your responsibilities:
1. Answer questions about the threats clearly and accurately.
2. Identify threats pytm may have missed, especially LLM-specific threats such as:
   - Prompt Injection (LLM01): user input overriding system instructions
   - Sensitive Information Disclosure (LLM02): model revealing context data
   - Model Denial of Service (LLM04): adversarial prompts causing token overuse
   - Insecure Output Handling (LLM05): agent output rendered without sanitization
3. Recommend specific, actionable mitigations using STRIDE categories.
4. When asked to prioritize, use Risk = Likelihood x Impact.
5. Keep responses concise but precise. Use bullet points for lists.
6. If uncertain, say so rather than guessing.
7. Ground all answers in the system described in the threat report.""",
)