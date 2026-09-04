class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.var_age: int = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm,", end='')
        print(f' {self.var_age} days old')

    def age(self) -> None:
        self.var_age += 1

    def grow(self, growth_p_d: float = 0.8) -> None:
        self.height += growth_p_d
        self.age()


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    initial = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.show()
    print(f"Growth this week: {round(rose.height - initial, 2)}cm")
