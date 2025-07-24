from clan.agents.base_agent import BaseAgent
from clan.llm import LLMClient
import re

class SummaryAgent(BaseAgent):
    def __init__(self, llm_client=None, tools=None, memory=None, config=None):
        super().__init__(role="Summary Agent", tools=tools, memory=memory, config=config or {})
        self.llm = llm_client or LLMClient()

    def act(self, current_summary, last_task_description, context=None):
        prompt = (
            "Given the following project summary and the latest task description, "
            "generate an updated summary that reflects the new project state.\n"
            f"Current summary:\n{current_summary}\n"
            f"Latest task description:\n{last_task_description}\n"
            "Updated summary:"
        )
        new_summary = self.llm.generate(prompt)
        new_summary = re.sub(r'<think>[\s\S]*?</think>', '', new_summary, flags=re.IGNORECASE)
        self.remember({"current_summary": current_summary, "last_task_description": last_task_description, "updated_summary": new_summary})
        return new_summary.strip() 