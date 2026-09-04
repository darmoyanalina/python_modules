from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    def describe(self) -> str:
        msg: str = f"{self.name} is a {self.type} type Creature"
        return msg

    @abstractmethod
    def attack(self) -> str:
        ...


class Flameling(Creature):
    def attack(self) -> str:
        msg: str = f"{self.name} uses Ember!"
        return msg


class Pyrodon(Creature):
    def attack(self) -> str:
        msg: str = f"{self.name} uses Flamethrower!"
        return msg


class Aquabub(Creature):
    def attack(self) -> str:
        msg: str = f"{self.name} uses Water Gun!"
        return msg


class Torragon(Creature):
    def attack(self) -> str:
        msg: str = f"{self.name} uses Hydro Pump!"
        return msg
