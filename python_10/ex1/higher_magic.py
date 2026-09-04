from typing import Any, Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"{target} is hit by a fireball for {power} damage!"


def spell_combiner(spell1: Callable[..., str],
                   spell2: Callable[..., str]) -> Callable[..., Any]:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("The arguments must be callable")

    def combine(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combine


def power_amplifier(base_spell: Callable[..., str],
                    multiplier: int) -> Callable[..., str]:
    if not callable(base_spell):
        raise TypeError("The first argument must be callable")

    def mult(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return mult


def conditional_caster(condition: Callable[..., Any],
                       spell: Callable[..., Any]) -> Callable[..., Any]:
    if not callable(condition) or not callable(spell):
        raise TypeError("The arguments must be callable")

    def func(target: str, power: int) -> Any:
        if condition(power):
            return spell(target, power)
        return "Spell fizzled"
    return func


def spell_sequence(spells: list[Callable[..., Any]]) -> Callable[..., Any]:
    for spell in spells:
        if not callable(spell):
            raise TypeError("The argument must be callable")

    def cast(target: str, power: int) -> list[str]:
        res: list[str] = []
        for item in spells:
            res.append(item(target, power))
        return res
    return cast


if __name__ == "__main__":
    test_values = [12, 18, 25]
    test_targets = ["Dragon", "Goblin", "Wizard", "Knight"]
    target: str = test_targets[0]
    power: int = test_values[1]
    print("\nTesting spell combiner...")
    combined: Callable[..., Any] = spell_combiner(heal, fireball)
    res: tuple[str, str] = combined(target, power)
    print(", ".join(res))
    print("\nTesting power amplifier...")
    amplify: Callable[..., Any] = power_amplifier(fireball, 3)
    print(f"Initial power - {power}\n{amplify(target, power)}")
    print("\nTesting conditional caster...")
    cond_func: Callable[..., Any] = conditional_caster(lambda y: y > 15, heal)
    print(cond_func(target, power))
    print("\nTesting spell sequence...")
    spells: list[Callable[..., str]] = [fireball, heal]
    sp_seq: Callable[..., Any] = spell_sequence(spells)
    print("\n".join(sp_seq(target, power)))
