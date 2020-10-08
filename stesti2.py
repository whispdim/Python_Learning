#Šťastný a bohatý nový
print("Zadej ANO, nebo NE")
stastný_retezec = input("Jsi šťasntý?")

if stastný_retezec == 'ano' or stastný_retezec == 'ANO' or stastný_retezec == 'Ano':
    stastný = True
elif stastný_retezec == 'ne' or stastný_retezec == 'NE' or stastný_retezec == 'Ne':
    stastný = False
else:
    print("Nerozumím")

bohatý_retezec = input("Jsi bohatý?")

if bohatý_retezec == 'ano' or bohatý_retezec == 'ANO' or bohatý_retezec == 'Ano':
    bohatý = True
elif bohatý_retezec == 'ne' or bohatý_retezec == 'NE' or bohatý_retezec == 'Ne':
    bohatý = False
else:
    print("Nerozumím")

if stastný and bohatý:
    print("Gratuluji!!!")
elif stastný:
    print("Zkus míň utrácet")
elif bohatý:
    print("Zkus se víc usmívat")
else:
    print("To je mi líto")