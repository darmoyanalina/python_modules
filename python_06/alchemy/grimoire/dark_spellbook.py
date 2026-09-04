from .dark_validator import validate_ingredients


def dark_spell_allowed_ingridients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validate: str = validate_ingredients(ingredients)
    if validate.split(" - ")[1] == "VALID":
        return f"Spell recorded: {spell_name} ({validate})"
    return f"Spell rejected: {spell_name} ({validate})"
