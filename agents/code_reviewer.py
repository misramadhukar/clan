from clan.agents.core.base_agent import BaseAgent
from clan.llm import LLMClient
from clan.config import PROMPT_TEMPLATES
import re

class CodeReviewerAgent(BaseAgent):
    def __init__(self, tools=None, memory=None, config=None):
        super().__init__(role="Code Reviewer Agent", tools=tools, memory=memory, config=config or {})

    def act(self, code, context=None):
        if "code_reviewer" not in self.config:
            raise KeyError("'code_reviewer' prompt template missing from config. Please add it to config.py and ensure it is passed to the agent.")
        prompt_template = self.config["code_reviewer"]
        prompt = prompt_template.format(code=code)
        review = self.llm.generate(prompt)
        review = re.sub(r'<think>[\s\S]*?</think>', '', review, flags=re.IGNORECASE)
        self.remember({"code": code, "review": review})
        return review 