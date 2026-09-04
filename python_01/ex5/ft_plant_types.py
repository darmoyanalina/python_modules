class Plant:
    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        self._name: str = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
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


class Flower(Plant):
    def __init__(self, color: str, name: str,
                 height: float = 0, age: int = 0) -> None:
        super().__init__(name, height, age)
        self._color = color

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

    def bloom(self) -> None:
        print(f"{self._name} has not bloomed yet")
        print(f"[asking the {self._name} to bloom]")
        self.show()
        print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self, trunk_diam: float, name: str, height: float = 0, age: int = 0
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diam

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{round(self.get_height(), 2)}", end="")
        print(f"cm long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        harv_seas: str,
        height: float = 0,
        age: int = 0,
        nut_val: int = 0,
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harv_seas
        self._nutritional_value = nut_val

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1


if __name__ == "__main__":
    rose = Flower(
        "Red",
        "Rose",
        15.0,
        10,
    )
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    rose.bloom()
    print("\n=== Tree")
    oak = Tree(5.0, "Oak", 200.0, 365)
    oak.show()
    oak.produce_shade()
    print("\n=== Vegetables")
    tomato = Vegetable("Tomato", "April", 5.0, 10)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow(2.1)
    tomato.show()
