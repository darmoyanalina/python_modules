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
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    print("=== Plant Factory Output ===")
    print("Created: ", end='')
    rose.show()
    print("Created: ", end='')
    oak.show()
    print("Created: ", end='')
    cactus.show()
    print("Created: ", end='')
    sunflower.show()
    print("Created: ", end='')
    fern.show()
