from abc import ABC, abstractmethod
from ex1 import HealCapability, TransformCapability
from ex0 import Creature
from typing import Any


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Any) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise AttributeError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
                )
        else:
            print(creature.attack())

    def is_valid(self, creature: Any) -> bool:
        if isinstance(creature, Creature):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            nme: str = "aggressive"
            raise AttributeError(
                f"Invalid Creature '{creature.name}' for this {nme} strategy"
                )

    def is_valid(self, creature: Any) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        else:
            return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            nme: str = "defensive"
            raise AttributeError(
                f"Invalid Creature '{creature.name}' for this {nme} strategy"
                )

    def is_valid(self, creature: Any) -> bool:
        if isinstance(creature, HealCapability):
            return True
        else:
            return False
