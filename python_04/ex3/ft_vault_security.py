def secure_archive(
    name: str, act: str = "w", cont: str = "Default"
) -> tuple[bool, str]:
    tup: tuple[bool, str] = (False, cont)
    try:
        with open(name, act) as file:
            if act == "r":
                try:
                    filestr: str = file.read()
                    tup = (True, filestr)
                except IOError as e:
                    tup = (False, str(e))
                except UnicodeEncodeError as e:
                    tup = (False, str(e))
            else:
                try:
                    file.write(cont)
                    tup = (True, cont)
                except IOError as e:
                    tup = (False, str(e))
                except UnicodeEncodeError as e:
                    tup = (False, str(e))
    except IOError as e:
        tup = (False, str(e))
    finally:
        return tup


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("foo", "r"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("a.txt", "r"))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("a.txt", "w", "Content successfully written to file"))
