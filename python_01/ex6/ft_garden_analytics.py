class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow: int = 0
            self._age: int = 0
            self._show: int = 0
            self._shade: int = 0

    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        self._name: str = name
        self.set_height(height)
        self.set_age(age)
        self._stats: Plant.Statistics = self.Statistics()

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
        self._stats._show += 1
        print(f"{self._name}: {round(self.get_height(), 2)}cm,", end="")
        print(f" {self.get_age()} days old")

    def age(self) -> None:
        self._stats._age += 1
        self.set_age(self.get_age() + 1)

    def grow(self, growth_p_d: float = 0.8) -> None:
        self._stats._grow += 1
        self.set_height(self.get_height() + growth_p_d)

    @staticmethod
    def age_checker(age: int) -> bool:
        print(f"Is {age} days more than a year? -> ", end="")
        if age > 365:
            print("True")
            return True
        print("False")
        return False

    @classmethod
    def create(cls) -> "Plant":
        return cls("Unknown plant")


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


class Seed(Flower):
    def __init__(self, color: str, name: str,
                 height: float = 0, age: int = 0) -> None:
        super().__init__(color, name, height, age)
        self._seeds: int = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42


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
        self._stats._shade += 1
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


def display_stats(plant: Plant) -> None:
    print(f"Stats: {plant._stats._grow} grow,", end="")
    print(f"{plant._stats._age} age, {plant._stats._show} show")
    if plant.__class__ == Tree:
        print(f"{plant._stats._shade} shade")


if __name__ == "__main__":
    rose = Flower(
        "red",
        "Rose",
        15.0,
        10,
    )
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.age_checker(30)
    Plant.age_checker(400)
    print("\n=== Flower")
    rose.show()
    rose.grow(13)
    rose.bloom()
    display_stats(rose)
    print("\n=== Tree")
    oak = Tree(5.0, "Oak", 200.0, 365)
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)
    print("\n=== Seed")
    sunflower = Seed("yellow", "Sunflower", 80.0, 45)
    sunflower.show()
    sunflower.grow(30)
    sunflower.age()
    sunflower.bloom()
    display_stats(sunflower)
    print("\n=== Anonymous")
    unknown = Plant.create()
    unknown.show()
    display_stats(unknown)
