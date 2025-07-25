from clan.agents.core.base_agent import BaseAgent
from clan.llm import LLMClient

class CommandRunnerAgent(BaseAgent):
    def __init__(self, llm_client=None, tools=None, memory=None, config=None):
        super().__init__(role="Command Runner Agent", tools=tools, memory=memory, config=config or {})
        self.llm = llm_client or LLMClient()

    def act(self, task_description, context=None):
        shell_type = (context or {}).get("shell", "bash")
        prompt = (
            f"You are an expert at writing shell commands. Given the following task, generate the most appropriate command for the specified shell.\n"
            f"Task: {task_description}\n"
            f"Shell: {shell_type}\n"
            f"Context: {context or ''}\n"
            "Return ONLY the command as a single line, no explanation."
        )
        command = self.llm.generate(prompt)
        self.remember({"task": task_description, "shell": shell_type, "command": command})
        return {"command": command.strip(), "shell": shell_type} 