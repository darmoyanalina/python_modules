class Plant:
    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        self._name: str = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"\nHeight updated: {self.get_height()}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self.get_age()} days")
        else:
            print(f"{self._name}:  Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {round(self.get_height(), 2)}cm,", end="")
        print(f" {self.get_age()} days old")

    def age(self) -> None:
        self.set_age(self.get_age() + 1)

    def grow(self, growth_p_d: float = 0.8) -> None:
        self.set_height(self.get_height() + growth_p_d)
        self.age()


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end='')
    rose.show()
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-25)
    rose.set_age(-30)
    print("\nCurrent state: ", end='')
    rose.show()
