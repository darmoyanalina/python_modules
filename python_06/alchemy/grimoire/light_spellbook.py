def light_spell_allowed_ingridients() -> list[str]:
    return ["earth", "air", "fire", "water"]


from .light_validator import validate_ingredients  # noqa: E402


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validate: str = validate_ingredients(ingredients)
    if validate.split(" - ")[1] == "VALID":
        return f"Spell recorded: {spell_name} ({validate})"
    return f"Spell rejected: {spell_name} ({validate})"
