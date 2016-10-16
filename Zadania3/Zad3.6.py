import sys
# program przyjmuje dwa argumenty; szerokosci i wysokosci, bedacymi liczbami calkowitymi

szerokosc = int(sys.argv[1])
wysokosc = int(sys.argv[2])

linijka="+-"*szerokosc+"+\n"+"| "*szerokosc+"|\n"
linijka =linijka*wysokosc+"+-"*szerokosc+"+"

print(linijka)
