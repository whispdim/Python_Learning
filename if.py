# Tento program počítá obvod a obsah čtverce.
strana = float(input("Zadej číslo"))  # v centimetrech
if strana < 0:
    print("Zadej kladné číslo")
else:
    print("Obvod čtverce se stranou", strana, "cm je", strana * 4, "cm")
    print("Obsah čtverce se stranou", strana, "cm je", strana**2, "cm2")