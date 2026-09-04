import sys
import os
import site

if __name__ == "__main__":
    cur: str = sys.executable
    vnv: str = os.environ.get("VIRTUAL_ENV", "None detected")
    if sys.prefix == sys.base_prefix:
        status: str = "You're still plugged in"
        is_in_vnv: bool = False
    else:
        status = "Welcome to the construct"
        is_in_vnv = True
    print(f"MATRIX STATUS: {status}")
    print(f"\nCurrent python: {cur}")
    print(f"Virtual environment: {os.path.basename(vnv)}")
    if is_in_vnv:
        print(f"Environment Path: {vnv}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("\nPackage installation path:")
        print(site.getsitepackages()[0])
    else:
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python3 -m virtualenv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")
