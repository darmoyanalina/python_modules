from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        flameling: Flameling = Flameling("Flameling", "Fire")
        return flameling

    def create_evolved(self) -> Pyrodon:
        pyrodon: Pyrodon = Pyrodon("Pyrodon", "Fire/Flying")
        return pyrodon


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        aquabub: Aquabub = Aquabub("Aquabub", "Water")
        return aquabub

    def create_evolved(self) -> Torragon:
        torragon: Torragon = Torragon("Torragon", "Water")
        return torragon
