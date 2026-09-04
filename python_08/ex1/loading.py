def imports() -> bool:
    all_imported: bool = True
    try:
        import pandas as pd
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    except ImportError as e:
        all_imported = False
        print(f"[KO] pandas - {e}")
    try:
        import numpy as np
        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
    except ImportError as e:
        all_imported = False
        print(f"[KO] numpy - {e}")
    try:
        import matplotlib as plt
        print(f"[OK] matplotlib ({plt.__version__}) - Visualization ready")
    except ImportError as e:
        all_imported = False
        print(f"[KO] matplotlib - {e}")
    return all_imported


def matrix_analyze() -> bool:
    print("\nChecking dependencies:")
    state: bool = True
    if imports():
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        matrix = np.random.randint(0, 100, size=(1000, 2))
        df = pd.DataFrame(matrix, columns=["x", "y"])
        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")
        df = df.sort_values(by="x")
        print("Generating visualization...")
        plt.plot(df["x"], df["y"])
        plt.savefig("matrix_analysis.png")
    else:
        print("\nMissing dependencies detected!")
        print("\nOption 1 - Install with pip:")
        print("  pip install -r requirements.txt")
        print("  python3 loading.py")
        print("\nOption 2 - Install with Poetry:")
        print("  poetry install")
        print("  poetry run python loading.py")
        print("\nEnd of program!")
        state = False
    return state


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    res: bool = matrix_analyze()
    if res:
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
