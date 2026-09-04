import sys


def get_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}
    i: int = 1
    n = len(sys.argv)
    while i < n:
        try:
            tmp = sys.argv[i].split(":")
            if len(tmp) != 2:
                raise ValueError
            try:
                if tmp[0] in inventory:
                    raise NameError
                inventory[tmp[0]] = int(tmp[1])
            except ValueError as e:
                print(f"Quantity error for '{tmp[0]}': {e}")
            except NameError:
                print(f"Redundant item '{tmp[0]}' - discarding")
        except ValueError:
            print(f"Error - invalid parameter '{tmp[0]}'")
        i += 1
    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = get_inventory()
    print(f"Got inventory: {inventory}")
    keys: list[str] = list(inventory.keys())
    values: list[int] = list(inventory.values())
    summ: int = sum(values)
    max_val: int = 0
    max_it: str = ""
    print(f"Item list: {keys}")
    print(f"Total quantity of the {len(keys)} items: {summ}")
    for key in inventory:
        if inventory[key] > max_val:
            max_val = inventory[key]
            max_it = key
        print(f"Item {key} represents ", end="")
        print(f"{round((inventory[key] / summ) * 100, 1)}%")
    print(f"Item most abundant: {max_it} with quantity {max_val}")
    min_val: int = max_val
    min_it: str = ""
    for key in inventory:
        if inventory[key] < min_val:
            min_val = inventory[key]
            min_it = key
    print(f"Item least abundant: {min_it} with quantity {min_val}")
    a: dict[str, int] = {"magic_item": 1}
    inventory.update(a)
    print(f"Updated inventory: {inventory}")
