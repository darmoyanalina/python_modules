import math


def get_player_pos() -> tuple[float, float, float]:
    try:
        coords: str = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        splitted: list[str] = coords.split(",")
        lst: list[float] = []
        i = 0
        if len(splitted) != 3:
            raise TypeError
        while i < len(splitted):
            lst.append(float(splitted[i]))
            i += 1
        coordinates: tuple[float, float, float] = (lst[0], lst[1], lst[2])
    except TypeError:
        print("Invalid syntax")
        coordinates = get_player_pos()
    except ValueError as e:
        msg: str = str(e)
        print(f"Error on parameter {msg.split(':')[1]}: {e}")
        coordinates = get_player_pos()
    return coordinates


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    coordinates: tuple[float, float, float] = get_player_pos()
    x1, y1, z1 = coordinates
    print(f"Got a first tuple: {coordinates}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {round(math.sqrt(x1**2 + y1**2 + z1**2), 4)}")
    print("\nGet a second set of coordinates")
    coordinates2: tuple[float, float, float] = get_player_pos()
    x2, y2, z2 = coordinates2
    print("Distance between the 2 sets of coordinates: ", end="")
    print(round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2), 4))
