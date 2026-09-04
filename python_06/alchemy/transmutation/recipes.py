from ..elements import create_air
from alchemy.potions import strength_potion


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: brew"
        + f"' {create_air()}' and '{strength_potion()}'"
        + " with 'Fire element created' and 'Water element"
        + " created' mixed with 'Fire element created'"
    )
