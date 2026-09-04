from typing import Any, Callable
from functools import wraps
import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}")
        start: float = time.perf_counter()
        res: Callable[..., Any] = func(*args, **kwargs)
        end: float = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return res

    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(power: int, *args: Any, **kwargs: Any) -> str:
            if power >= min_power:
                res: str = func(power, *args, **kwargs)
            else:
                return "Insufficient power for this spell"
            return res

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(max_attempts):
                try:
                    res: Any = func(*args, **kwargs)
                    return res
                except Exception:
                    print("Spell failed, retrying... ", end="")
                    print(f"(attempt {i + 1}/{max_attempts})")
            return "Spell casting failed after max_attempts attempts"

        return wrapper

    return decorator


@power_validator(10)
def cast_sp(power: int, spell_name: str) -> str:
    return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def cast_earthquake(spell: str) -> str:
    return f"{spell} has been performed!"


@power_validator(21)
def amplified_cast(power: int, spell: str) -> str:
    return f"The {spell} cast with the power {power}"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and name.replace(" ", "").isalpha():
            return True
        return False

    def cast_spell(self, spell_name: str, power: int) -> str:
        return str(cast_sp(power, spell_name))


if __name__ == "__main__":
    test_powers = [16, 20, 28, 22]
    spell_names = ["earthquake", "lightning", "darkness", "tsunami"]
    mage_names = ["Sage", "Luna", "Kai", "River", "Jordan", "Ash"]
    invalid_names = ["Jo", "A", "Alex123", "Test@Name"]

    print("Testing spell_timer...")
    result: Any = cast_earthquake("Earthquake")
    print(f"Result: {result}")

    print("\nTesting power_validator...")
    for i in range(4):
        print(amplified_cast(test_powers[i], spell_names[i]))

    print("\nTesting retry_spell...")
    attempt_count: list[int] = [0]

    @retry_spell(3)
    def unstable_spell() -> str:
        attempt_count[0] += 1
        if attempt_count[0] < 3:
            raise Exception("Spell unstable!")
        return "Darkness surge complete!"

    print(unstable_spell())

    @retry_spell(3)
    def always_fails() -> str:
        raise Exception("Too weak!")

    print(always_fails())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    for name in mage_names:
        print(f"  {name}: {guild.validate_mage_name(name)}")
    for name in invalid_names:
        print(f"  {name}: {guild.validate_mage_name(name)}")
    print()
    for i in range(4):
        print(guild.cast_spell(spell_names[i], test_powers[i]))
