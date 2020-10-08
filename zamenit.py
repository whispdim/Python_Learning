# tento kod bude měnit zadane pismeno na jine
slovo = 'Cherrissimo'
print(len(slovo))
číslo = 3
písmeno = input('Zadej písmeno ')
def záměna(a,b,c):
    return slovo[:3-1] + písmeno + slovo[3:]
print(záměna(slovo,číslo,písmeno))
