"""
Abstract base class for language-specific agent factories. Implementations should provide methods to create code-related agents for a specific language.
"""
from abc import ABC, abstractmethod
from clan.agents.developer import DeveloperAgent
from clan.agents.code_reviewer import CodeReviewer
from clan.agents.unit_tester import UnitTester

class AgentFactory(ABC):
    @abstractmethod
    def create_developer_agent(self) -> DeveloperAgent:
        pass

    @abstractmethod
    def create_code_reviewer(self) -> CodeReviewer:
        pass

    @abstractmethod
    def create_unit_tester(self) -> UnitTester:
        pass

    @abstractmethod
    def create_transformer_agent(self) -> "TransformerAgent":
        pass 