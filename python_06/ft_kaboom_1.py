print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")


import alchemy.grimoire.dark_spellbook as dark  # noqa: E402

print(dark.dark_spell_record("Dark", "Bats, frogs and fire"))
