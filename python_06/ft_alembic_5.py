from alchemy import create_air

print("=== Alembic 5 ===")
print("Accessing the alchemy module using 'from alchemy import ...'")
air: str = create_air()
print(f"Testing create_water: {air}\n")
