a = float(input("Zadej stranu obdelníka a"))
b = float(input("Zadej stranu obdelníka b"))
if a < 0 or b < 0:
    print("strana musí být kladná")
else:
    print("Obsah obdelníka je roven", a * b * 2, "cm")