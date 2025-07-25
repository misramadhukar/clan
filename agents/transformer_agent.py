from clan.agents.core.base_agent import BaseAgent
from clan.llm import LLMClient
from clan.config import PROMPT_TEMPLATES
import re

class TransformerAgent(BaseAgent):
    def __init__(self, llm_client=None, tools=None, memory=None, config=None):
        super().__init__(role="Transformer Agent", tools=tools, memory=memory, config=config or PROMPT_TEMPLATES)
        self.llm = llm_client or LLMClient()

    def act(self, code, context=None):
        prompt_template = self.config["transformer_agent"]
        prompt = prompt_template.format(code=code, context=context or "")
        improved_code = self.llm.generate(prompt)
        improved_code = re.sub(r'<think>[\s\S]*?</think>', '', improved_code, flags=re.IGNORECASE)
        self.remember({"code": code, "improved_code": improved_code})
        return improved_code.strip() 