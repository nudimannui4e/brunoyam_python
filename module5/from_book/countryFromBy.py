# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------

class CountryFromBy:
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)


c = CountryFromBy(1, 10)
print(f'Значение: {c.val}')
print(f'Инкремент: {c.incr}')
print(c)
c.increase()
print(f'Значение: {c.val}')
print(f'Инкремент: {c.incr}')
