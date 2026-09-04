from .light_spellbook import light_spell_allowed_ingridients


def validate_ingredients(ingredients: str) -> str:
    ing_list: list[str] = ingredients.replace(",", "").split(" ")
    allowed: list[str] = light_spell_allowed_ingridients()
    for i in ing_list:
        for j in allowed:
            if i.upper() == j.upper():
                return ingredients + " - VALID"
    return ingredients + " - INVALID"
