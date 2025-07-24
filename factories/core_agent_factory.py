from clan.agents.file_agent import FileAgent
from clan.agents.task_planner import TaskPlannerAgent
from clan.agents.summary_agent import SummaryAgent
from clan.agents.user_interaction_agent import UserInteractionAgent

class CoreAgentFactory:
    def __init__(self, llm_client=None, config=None):
        self.llm_client = llm_client
        self.config = config

    def create_file_agent(self, project_state=None):
        return FileAgent(project_state=project_state, llm_client=self.llm_client, config=self.config)

    def create_task_planner(self):
        return TaskPlannerAgent(llm_client=self.llm_client, config=self.config)

    def create_summary_agent(self):
        return SummaryAgent(llm_client=self.llm_client, config=self.config)

    def create_user_interaction_agent(self):
        return UserInteractionAgent(config=self.config) 