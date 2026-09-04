from typing import Any, Callable
from functools import reduce, partial, lru_cache, singledispatch
import operator


def base(power: int, element: str, target: str) -> str:
    return element + " enchants the " + target + " with a power " + str(power)


def spell_reducer(spells: list[int], operation: str) -> int:
    sep: dict[str, Callable[..., Any]] = {
        "max": max,
        "min": min,
        "multiply": operator.mul
    }
    op: Any = sep.get(operation) or getattr(operator, operation, None)
    if op is None:
        raise ValueError(f"Unknown operation {operation}")
    if len(spells) == 0:
        return 0
    return reduce(op, spells)


def partial_enchanter(base_enchantment: Callable[..., Any]
                      ) -> dict[str, Callable[..., Any]]:
    elements: list[str] = ["Fire", "Water", "Earth"]
    res: dict[str, Callable[..., Any]] = {}
    res[elements[0]] = partial(base_enchantment, 50, elements[0])
    res[elements[1]] = partial(base_enchantment, 50, elements[1])
    res[elements[2]] = partial(base_enchantment, 50, elements[2])
    return res


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base(arg: Any) -> str:
        raise NotImplementedError(f"No implementation for type {type(arg)}")

    @base.register
    def _(damage_spell: int) -> str:
        return str(damage_spell) + " damage"

    @base.register
    def _(enchantment: str) -> str:
        return "*" + enchantment + "*"

    @base.register(list)
    def _(multi_cast: list[Any]) -> str:
        return str(len(multi_cast)) + " spells"
    return base


if __name__ == "__main__":
    spell_powers = [44, 44, 31, 23, 26, 37]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [15, 18, 13]

    print("Testing spell_reducer...")
    for op in operations:
        print(f"  {op}: {spell_reducer(spell_powers, op)}")
    try:
        spell_reducer(spell_powers, "addd")
    except ValueError as e:
        print(f"  Error caught: {e}")

    print("\nTesting partial_enchanter...")
    enchant: dict[str, Callable[..., Any]] = partial_enchanter(base)
    for element, func in enchant.items():
        print(f"  {element}: {func('Nova')}")

    print("\nTesting memoized_fibonacci...")
    for n in fibonacci_tests:
        print(f"  Fib({n}): {memoized_fibonacci(n)}")
    print(f"  Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell_dispatcher...")
    dispatch = spell_dispatcher()
    print(f"  int:  {dispatch(42)}")
    print(f"  str:  {dispatch('fireball')}")
    print(f"  list: {dispatch(['fire', 'ice'])}")
    try:
        dispatch(3.14)
    except NotImplementedError as e:
        print(f"  Error caught: {e}")
