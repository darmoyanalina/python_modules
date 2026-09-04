from ex0 import FlameFactory, AquaFactory, Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy
from ex2 import DefensiveStrategy, AggressiveStrategy


def battle(lst: list[tuple[Creature, BattleStrategy]]) -> None:
    i: int = 0
    print("*** Tournament ***")
    print(f"{len(lst)} opponents involved\n")
    while i < len(lst) - 1:
        j: int = 1
        while i + j < len(lst):
            print("* Battle *")
            print(lst[i][0].describe())
            print(" vs.")
            print(lst[i+j][0].describe())
            print(" now fight!")
            try:
                lst[i][1].act(lst[i][0])
                lst[i+j][1].act(lst[i+j][0])
            except AttributeError as e:
                print(f"Battle error, aborting tournament: {e}")
            finally:
                j += 1
                print()
        i += 1


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    flameling: Creature = FlameFactory().create_base()
    aquabub: Creature = AquaFactory().create_base()
    sproutling = HealingCreatureFactory().create_base()
    shiftling = TransformCreatureFactory().create_base()
    normal: BattleStrategy = NormalStrategy()
    defensive: BattleStrategy = DefensiveStrategy()
    aggressive: BattleStrategy = AggressiveStrategy()
    tour00: tuple[Creature, BattleStrategy] = (flameling, normal)
    tour01: tuple[Creature, BattleStrategy] = (sproutling, defensive)
    tour0: list[tuple[Creature, BattleStrategy]] = [tour00, tour01]
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle(tour0)
    tour10: tuple[Creature, BattleStrategy] = (flameling, aggressive)
    tour11: tuple[Creature, BattleStrategy] = (sproutling, defensive)
    tour1: list[tuple[Creature, BattleStrategy]] = [tour10, tour11]
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(tour1)
    tour20: tuple[Creature, BattleStrategy] = (aquabub, normal)
    tour21: tuple[Creature, BattleStrategy] = (sproutling, defensive)
    tour22: tuple[Creature, BattleStrategy] = (shiftling, aggressive)
    tour2: list[tuple[Creature, BattleStrategy]] = [tour20, tour21, tour22]
    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(tour2)
