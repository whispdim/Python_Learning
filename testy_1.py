def nacti_cislo():
    while True:
        odpoved = input('Zadej číslo: ')
        if obsahuje_jen_cislice(odpoved):
            return int(odpoved)  # máme výsledek, funkce končí
        else:
            print('To nebylo číslo!')
            # ... a zeptáme se znovu -- cyklus `while` pokračuje