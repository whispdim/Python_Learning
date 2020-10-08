# tento program se zeptá na tvé jméno, pak příjmení a pak ti stavojí tvé iniciály
'''První je potřeba zjistit tvé jméno a pak příjmení'''
jméno = input('Jaké je tvé křesní jméno? ')
příjmení = input('Jaké je tvé příjmení? ')
aa = jméno.upper()[0]
bb = příjmení.upper()[0]
print(jméno + ' ' + příjmení)
print('Tvé iniciály jsou', aa + bb)