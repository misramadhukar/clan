"""
Abstract base class for language-specific agent factories. Implementations should provide methods to create code-related agents for a specific language.
"""
from abc import ABC, abstractmethod
from clan.agents.developer import DeveloperAgent
from clan.agents.code_reviewer import CodeReviewerAgent
from clan.agents.unit_tester import UnitTesterAgent

class AgentFactory(ABC):
    @abstractmethod
    def create_developer_agent(self) -> DeveloperAgent:
        pass

    @abstractmethod
    def create_code_reviewer(self) -> CodeReviewerAgent:
        pass

    @abstractmethod
    def create_unit_tester(self) -> UnitTesterAgent:
        pass

    @abstractmethod
    def create_transformer_agent(self) -> "TransformerAgent":
        pass 