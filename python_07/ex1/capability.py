from abc import ABC, abstractmethod
from ex0 import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        ...


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.is_reverted: bool = True

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...


class Sproutling(Creature, HealCapability):
    def attack(self) -> str:
        msg: str = f"{self.name} uses Vine Whip!"
        return msg

    def heal(self) -> str:
        msg: str = f"{self.name} heals itself with a small amount"
        return msg


class Bloomelle(Creature, HealCapability):
    def attack(self) -> str:
        msg: str = f"{self.name} uses Petal Dance!"
        return msg

    def heal(self) -> str:
        msg: str = f"{self.name} heals itself and others for a large amount"
        return msg


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_reverted = False
        msg: str = f"{self.name} shifts into a sharper form!"
        return msg

    def revert(self) -> str:
        self.is_reverted = True
        msg: str = f"{self.name} returns to normal."
        return msg

    def attack(self) -> str:
        if self.is_reverted:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_reverted = False
        msg: str = f"{self.name} morphs into a dragonic battle form!"
        return msg

    def revert(self) -> str:
        self.is_reverted = True
        msg: str = f"{self.name} stabilizes its form."
        return msg

    def attack(self) -> str:
        if self.is_reverted:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"
