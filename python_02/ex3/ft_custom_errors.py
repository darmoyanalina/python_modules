class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def error_case_plant(status: int) -> None:
    if status <= 0:
        raise PlantError("The tomato plant is wilting!")


def error_case_water(water: int) -> None:
    if water < 35:
        raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    tomato_status = 0
    water = 5
    print("=== Custom Garden Errors Demo ===")
    try:
        print("\nTesting PlantError...")
        error_case_plant(tomato_status)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    try:
        print("\nTesting WaterError...")
        error_case_water(water)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    try:
        print("\nTesting catching all garden errors...")
        error_case_plant(tomato_status)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        error_case_water(water)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


test_errors()
