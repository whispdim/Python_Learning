stastna = input("Jsi šťastná/ý?")
bohata = input("Jsi bohatá/ý?")

if stastna == 'ano':
    if bohata =='ano':
        print("Gratuluji!!!")
    else:
        print("Zkus míň utrácet")
else:
    if bohata == 'ano':
        print("Zkus se víc usmívat")
    else:
        print("To je mi líto!!!")