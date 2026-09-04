class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f" Invalid plant name to water: '{plant_name}'")


def test_watering_system(plant_names: list[str]) -> None:
    print("Opening watering system")
    try:
        for i in plant_names:
            try:
                water_plant(i)
            except PlantError as e:
                print(f"Caught PlantError: {e}")
                print(".. ending tests and returning to main")
                return None
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    plant_names: list[str] = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(plant_names)
    print("\nTesting invalid plants...")
    plant_names = ["Tomato", "lettuce", "Carrots"]
    test_watering_system(plant_names)
    print("\nCleanup always happens, even with errors!")
