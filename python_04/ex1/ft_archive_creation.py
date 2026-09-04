import sys


def reader() -> str:
    filestr: str = ""
    try:
        file = open(sys.argv[1], "r")
        try:
            filestr = file.read()
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
            return filestr
    except IOError as e:
        print(f"Error opening file {str(e).split(':')[1]}: {e}\n")
    except Exception as e:
        print(f"Error opening file {str(e).split(':')[1]}: {e}\n")
    return filestr


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        filestr: str = reader()
        if filestr:
            lst: list[str] = filestr.splitlines()
            lst2: list[str] = [x + "#" for x in lst]
            print("\nTransform data:")
            print("---\n")
            for i in lst2:
                print(i)
            print("\n---")
            inp: str = input("Enter new file name (or empty): ")
            if not inp:
                print("Not saving data.")
            else:
                file = open(inp, "w")
                print(f"Saving data to '{inp}'")
                try:
                    for x in lst2:
                        file.write(x + "\n")
                    print(f"Data saved in file '{inp}'.")
                except IOError as e:
                    print(f"Error trying to write in a file: {e}")
    except ValueError:
        print("Usage: ft_ancient_text.py <file>\n")
