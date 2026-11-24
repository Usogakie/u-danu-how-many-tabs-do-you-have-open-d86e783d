import os

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# 317: an honest, lived-in tab hoard. Far above the handful of tabs most
# people keep open, so it reads as surprising, yet a count a real researcher
# with a few crowded browser windows could truly have open right now.
# Deliberately not round, not a joke number, and not an absurd shock figure.
COUNT = "317"


def main():
    assert COUNT.isdigit() and 1 <= len(COUNT) <= 5, "gate: 1-5 digit chars"
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(COUNT)


if __name__ == "__main__":
    main()
