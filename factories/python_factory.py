from clan.factories.core_agent_factory import CoreAgentFactory
from clan.factories.abstract_factory import AgentFactory
from clan.agents.developer import DeveloperAgent
from clan.agents.code_reviewer import CodeReviewer
from clan.agents.unit_tester import UnitTester
from clan.llm import LLMClient
from clan.config import PROMPT_TEMPLATES

class PythonAgentFactory(CoreAgentFactory, AgentFactory):
    """
    Factory for creating both core (language-agnostic) and Python-specific agents.
    """
    def __init__(self, llm_client=None, config=None):
        super().__init__(llm_client=llm_client, config=config)

    def create_developer_agent(self) -> DeveloperAgent:
        return DeveloperAgent(llm_client=self.llm_client, config=self.config)

    def create_code_reviewer(self) -> CodeReviewer:
        return CodeReviewer(llm_client=self.llm_client, config=self.config)

    def create_unit_tester(self) -> UnitTester:
        return UnitTester(llm_client=self.llm_client, config=self.config)

    def create_transformer_agent(self):
        from clan.agents.transformer_agent import TransformerAgent
        return TransformerAgent(llm_client=self.llm_client, config=self.config) 