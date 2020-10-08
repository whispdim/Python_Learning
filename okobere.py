from random import uniform

soucet = 0


while soucet < 21:
    print ('Máš', soucet, 'bodů')
    odpoved = input('Otočit kartu? Y/N ')
    if odpoved == 'Y' or odpoved == 'y':
        tah = int(uniform(2,11))
        print('Otočil jsi', tah)
        soucet = soucet + tah
    elif odpoved == 'N' or odpoved == 'n':
        break
    else:
        print('Odpovídej Y/N')

if soucet == 21:
    print('Jsi nejlepší!!!')
elif soucet > 21:
    print('Prohrál jsi!!!')
else:
    print('Chybělo jen', 21 - soucet)