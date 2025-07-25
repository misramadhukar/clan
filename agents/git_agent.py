from clan.agents.core.base_agent import BaseAgent
from clan.llm import LLMClient

class GitAgent(BaseAgent):
    def __init__(self, llm_client=None, tools=None, memory=None, config=None):
        super().__init__(role="Git Agent", tools=tools, memory=memory, config=config or {})
        self.llm = llm_client or LLMClient()

    def act(self, git_task, context=None):
        shell_type = (context or {}).get("shell", "bash")
        prompt = (
            f"You are an expert at writing git commands. Given the following task, generate the most appropriate git command for the specified shell.\n"
            f"Task: {git_task}\n"
            f"Shell: {shell_type}\n"
            f"Context: {context or ''}\n"
            "Return ONLY the command as a single line, no explanation."
        )
        command = self.llm.generate(prompt)
        self.remember({"task": git_task, "shell": shell_type, "command": command})
        return {"command": command.strip(), "shell": shell_type} 