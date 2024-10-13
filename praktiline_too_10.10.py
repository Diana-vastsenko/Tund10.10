"""Matemaatilised tehted"""


# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b
a=float(input("Sisesta a:"))
b=float(input("Sisesta b:"))
# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)
import math
c=math.sqrt(a**2 + b**2).__round__(2)
print(f"HUPOTEENUS: {c}")
print(f"pindala: {(a * b/2).__round__(2)}")
print(f"ümbermõõt: {(a + b + c).__round__(2)}")


