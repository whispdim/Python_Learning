def napis_score(nazev, skore):
    print(nazev, 'skore je', skore)
    if skore >= 1000:
        print('Světový rekord!')
    elif skore > 100:
        print('Super')
    elif skore > 10:
        print('Jde to')
    elif skore > 1:
        print('Aspoň něco')
    else:
        print('Snad příště')

napis_score('Tvoje', 234)
napis_score('Cizí', 3)