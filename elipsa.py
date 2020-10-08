from math import pi
# vzoreček pro výpočet obsahu elipsy A = pi * a * b

def obsah_elipsy(osax, osay):
    return int(pi * osax * osay)
print(obsah_elipsy(4,6))