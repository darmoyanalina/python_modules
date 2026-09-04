import alchemy.elements

print("=== Alembic 2 ===")
print("Accessing alchemy/elements.py using 'import ...' structure")
earth: str = alchemy.elements.create_earth()
print(f"Testing create_earth: {earth}\n")
