strana = float(input("Zadej kladné číslo"))
správné_cislo = strana > 0
if správné_cislo:
    print("Obvod čtverce se stranou", strana, "cm je", strana * 4, "cm")
    print("Obsah čtverce se stranou", strana, "cm je", strana**2, "cm2")
else:
    print("Strana musí být kladná, jinak z toho nebude čtverec!")
print("Děkujeme, že jste použili geometrickou kalkulačku")