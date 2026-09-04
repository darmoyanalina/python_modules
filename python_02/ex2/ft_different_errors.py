def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        x: float = 10 / 0
        print(x)
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        print("abc" + 5)
    else:
        return None


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    a = [0, 1, 2, 3, 4]
    for i in a:
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully")

    print("\nAll error types tested successfully!")


test_error_types()
