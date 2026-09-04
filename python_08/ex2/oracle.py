from dotenv import load_dotenv
import os

print("\nORACLE STATUS: Reading the Matrix...")
load_dotenv()
print("\nConfiguration loaded:")
mode: str | None = os.environ.get("MATRIX_MODE")
db_url: str | None = os.environ.get("DATABASE_URL")
api_key: str | None = os.environ.get("API_KEY")
log_lvl: str | None = os.environ.get("LOG_LEVEL")
zion_endp: str | None = os.environ.get("ZION_ENDPOINT")
try:
    if not (mode and db_url and api_key and log_lvl and zion_endp):
        raise EnvironmentError("[KO] Configurations not right")
    if mode == "development":
        print(f"Mode: {mode}")
        print(f"Database: Connected to {db_url.split('/')[-1]}")
        print("API Access: Authenticated")
        print(f"Log Level: {log_lvl}")
        print(f"Zion Network: {zion_endp}")
    elif mode == "production":
        print(f"Mode: {mode}")
        print("Database: Connected")
        print("API Access: Authenticated")
        print(f"Log Level: {log_lvl}")
        print("Zion Network: Online")
    print("\nThe Oracle sees all configurations.")
except EnvironmentError as e:
    print(e)
