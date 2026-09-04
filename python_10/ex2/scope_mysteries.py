from typing import Any, Callable


def mage_counter() -> Callable[..., int]:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[..., int]:
    def accumulate(pow: int) -> int:
        nonlocal initial_power
        initial_power += pow
        return initial_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[..., str]:

    def enchant(item: str) -> str:
        return enchantment_type + " " + item
    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    res: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        res[key] = value

    def recall(key: str) -> Any:
        try:
            return res[key]
        except KeyError:
            return "Memory not found"
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    initial_power = 100
    power_additions = [7, 10, 16, 8, 5]
    enchantment_types = ['Dark', 'Radiant', 'Shocking']
    items_to_enchant = ['Cloak', 'Amulet', 'Wand', 'Staff']
    counter_a: Callable[..., int] = mage_counter()
    counter_b: Callable[..., int] = mage_counter()
    print("Testing mage counter...")
    for i in range(2):
        print(f"counter_a call {int(i) + 1} - {counter_a()}")
    print(f"counter_b call 1 - {counter_b()}")
    print("\nTesting spell accumulator...")
    accumulate: Callable[..., int] = spell_accumulator(initial_power)
    for i in power_additions:
        print(f"Base {initial_power}, add {int(i)}: {accumulate(i)}")
    print("\nTesting enchantment factory...")
    enchant: Callable[..., str] = enchantment_factory(enchantment_types[0])
    for item in items_to_enchant:
        print(enchant(item))
    print("\nTesting memory vault...")
    store_recall: dict[str, Callable[..., Any]] = memory_vault()
    print("Store 'secret' = 42")
    store_recall["store"]("secret", 42)
    print(f"Recall 'secret': {store_recall['recall']('secret')}")
    print(f"Recall 'unknown': {store_recall['recall']('unknown')}")
