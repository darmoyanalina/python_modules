from .capability import Sproutling, Bloomelle, Shiftling, Morphagon
from ex0 import CreatureFactory


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        sproutling: Sproutling = Sproutling("Sproutling", "Grass")
        return sproutling

    def create_evolved(self) -> Bloomelle:
        bloomelle: Bloomelle = Bloomelle("Bloomelle", "Grass/Fairy")
        return bloomelle


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        shiftling: Shiftling = Shiftling("Shiftling", "Normal")
        return shiftling

    def create_evolved(self) -> Morphagon:
        morphagon: Morphagon = Morphagon("Morphagon", "Normal/Dragon")
        return morphagon
