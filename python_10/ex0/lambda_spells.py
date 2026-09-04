from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x["power"])


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    res: dict[str, Any] = {}
    res["max_power"] = max(mages, key=lambda x: x["power"])
    res["min_power"] = min(mages, key=lambda x: x["power"])
    res["avg_power"] = round(
        sum(x["power"] for x in mages) / len(mages), 2)
    return res


if __name__ == "__main__":
    artifacts: list[dict[str, Any]] = [
        {"name": "Shadow Blade", "power": 100, "type": "focus"},
        {"name": "Water Chalice", "power": 92, "type": "weapon"},
        {"name": "Wind Cloak", "power": 118, "type": "accessory"},
        {"name": "Fire Staff", "power": 81, "type": "armor"},
    ]
    mages = [
        {"name": "Sage", "power": 98, "element": "earth"},
        {"name": "Ember", "power": 98, "element": "shadow"},
        {"name": "Casey", "power": 79, "element": "wind"},
        {"name": "River", "power": 63, "element": "earth"},
        {"name": "Kai", "power": 69, "element": "wind"},
    ]
    spells = ["meteor", "heal", "fireball", "flash"]
    art_sorted: list[dict[str, Any]] = artifact_sorter(artifacts)
    pow_filtered: list[dict[str, Any]] = power_filter(mages, 70)
    spells_trasformed: list[str] = spell_transformer(spells)
    print("\nTesting artifact sorter...")
    for x in art_sorted:
        print(f'{x["name"]} - power {x["power"]}')
    print("\nTesting power filter...")
    for x in pow_filtered:
        print(f'{x["name"]} - power {x["power"]}')
    print("\nTesting spell transformer...")
    print(" ".join(spells_trasformed))
