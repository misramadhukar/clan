from clan.agents.core.base_agent import BaseAgent
from clan.llm import LLMClient

class GrepSearchAgent(BaseAgent):
    def __init__(self, llm_client=None, tools=None, memory=None, config=None):
        super().__init__(role="Grep Search Agent", tools=tools, memory=memory, config=config or {})
        self.llm = llm_client or LLMClient()

    def act(self, pattern, search_path=".", context=None):
        shell_type = (context or {}).get("shell", "bash")
        prompt = (
            f"You are an expert at writing grep commands. Given the following pattern and search path, generate the most appropriate grep command for the specified shell.\n"
            f"Pattern: {pattern}\n"
            f"Search path: {search_path}\n"
            f"Shell: {shell_type}\n"
            f"Context: {context or ''}\n"
            "Return ONLY the command as a single line, no explanation."
        )
        command = self.llm.generate(prompt)
        self.remember({"pattern": pattern, "search_path": search_path, "shell": shell_type, "command": command})
        return {"command": command.strip(), "shell": shell_type} 