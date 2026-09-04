from elements import create_water


print("=== Alembic 1 ===")
print("Using: 'from ... import ...' structure to access elements.py")
water: str = create_water()
print(f"Testing create_water: {water}\n")
