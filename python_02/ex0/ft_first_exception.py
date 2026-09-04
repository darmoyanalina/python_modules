def input_temperature(temp_str: str) -> int:
    print(f"\nInput data is '{temp_str}'")
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    try:
        res: int = input_temperature("25")
        print(f"Temperature is now {res}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        res = input_temperature("abc")
        print(f"Temperature is now {res}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


test_temperature()
