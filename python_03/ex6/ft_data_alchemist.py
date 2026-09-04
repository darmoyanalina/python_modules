import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    initial: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"\nInitial list of players: {initial}")
    cap: list[str] = [x.capitalize() for x in initial]
    caped: list[str] = [x for x in initial if x == x.capitalize()]
    print(f"New list with all names capitalized: {cap}")
    print(f"New list of capitalized names only: {caped}")
    score_dict: dict[str, int] = {x: random.randint(0, 1000) for x in cap}
    print(f"\nScore dict: {score_dict}")
    average: float = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average}")
    high: dict[str, int] = {
        x: score_dict[x] for x in score_dict if score_dict[x] > average
    }
    print(f"High scores: {high}")
