import random


def get_player_achievments() -> set[str]:
    achievments: list[str] = [
        "Strategist",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Crafting Genius",
        "World Savior",
        "Hidden Path Finder",
        "Unstoppable",
        "Boss Slayer",
    ]
    n = len(achievments)
    num: int = random.randint(1, n)
    return set(random.sample(achievments, k=num))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    achievments: set[str] = {
        "Strategist",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Crafting Genius",
        "World Savior",
        "Hidden Path Finder",
        "Unstoppable",
        "Boss Slayer",
    }
    alice = get_player_achievments()
    bob = get_player_achievments()
    charlie = get_player_achievments()
    dylan = get_player_achievments()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print("\nAll distinct achievements: ", end="")
    print(set.union(alice, bob, charlie, dylan))
    print("\nCommon achievments: ", end='')
    print(set.intersection(alice, bob, charlie, dylan))
    print("\nOnly Alice has: ", end="")
    print(set.difference(alice, (bob | charlie | dylan)))
    print("Only Bob has: ", end="")
    print(set.difference(bob, (alice | charlie | dylan)))
    print("Only Charlie has: ", end="")
    print(set.difference(charlie, (bob | alice | dylan)))
    print("Only Dylan has: ", end="")
    print(set.difference(dylan, (bob | alice | charlie)))
    print("\nAlice is missing: ", end="")
    print(set.difference(achievments, alice))
    print("Bob is missing: ", end="")
    print(set.difference(achievments, bob))
    print("Charlie is missing: ", end="")
    print(set.difference(achievments, charlie))
    print("Dylan is missing: ", end="")
    print(set.difference(achievments, dylan))
