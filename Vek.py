# Toto je sranda příklad pro věk
vek = int(input("Zadej kolik ti je let?"))
if vek > 150:
    print("Z kterepák jsi planety?")
elif vek >= 18:
    print("Můžeme nabídnout vodku, džin, cider")
elif vek >= 1:
    print("Můžeme nabídnout vodu, čaj")
elif vek >= 0:
    print("Sunar už bohužel dosel")
else:
    print("Pro návštěvy z budoucnosti nic nemáme!")