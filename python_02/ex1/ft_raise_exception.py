def input_temperature(temp_str: str) -> int:
    print(f"\nInput data is '{temp_str}'")
    temp = int(temp_str)
    if temp >= 0 and temp <= 40:
        return temp
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
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
    try:
        res = input_temperature("100")
        print(f"Temperature is now {res}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        res = input_temperature("-50")
        print(f"Temperature is now {res}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


test_temperature()
