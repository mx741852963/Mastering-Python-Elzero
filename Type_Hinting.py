# ------------------
# -- Type Hinting --
# ------------------
def say_hello(name: str) -> str:
    return f"Hello {name}"


print(say_hello("John"))


def calculate(n1: int, n2: int) -> int:
    return n1 + n2


print(calculate(1, 2))
