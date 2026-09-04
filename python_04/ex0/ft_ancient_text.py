import sys


def reader() -> None:
    try:
        file = open(sys.argv[1], "r")
        try:
            filestr: str = file.read()
            print("---\n")
            print(filestr)
            print("---")
        except IOError as e:
            print(f"Error trying to read from a file: {e}")
        except UnicodeEncodeError as e:
            print(f"Error trying to read from a file: {e}")
        finally:
            print(f"File '{sys.argv[1]}' closed.")
            file.close()
    except IOError as e:
        print(f"Error opening file {str(e).split(':')[1]}: {e}\n")
    except Exception as e:
        print(f"Error opening file {str(e).split(':')[1]}: {e}\n")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        reader()
    except ValueError:
        print("Usage: ft_ancient_text.py <file>\n")
