from clan.agents.base_agent import BaseAgent
from clan.llm import LLMClient
from clan.config import PROMPT_TEMPLATES
import re

class UnitTester(BaseAgent):
    def __init__(self, llm_client=None, tools=None, memory=None, config=None):
        super().__init__(role="Unit Tester", tools=tools, memory=memory, config=config or PROMPT_TEMPLATES)
        self.llm = llm_client or LLMClient()

    def act(self, code, context=None):
        prompt_template = self.config["unit_tester"]
        prompt = prompt_template.format(code=code)
        tests = self.llm.generate(prompt)
        tests = re.sub(r'<think>[\s\S]*?</think>', '', tests, flags=re.IGNORECASE)
        self.remember({"code": code, "tests": tests})
        return tests 