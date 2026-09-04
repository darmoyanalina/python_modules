from alchemy.elements import create_air


print("=== Alembic 3 ===")
print("Using: 'from ... import ...' structure to access elements.py")
air: str = create_air()
print(f"Testing create_water: {air}\n")
