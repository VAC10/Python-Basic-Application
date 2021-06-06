# -*- coding: utf-8 -*-
#cmath modulunu programımıza import ettik.
import cmath
a=int(input("klavyeden 'a' degerini giriniz:"))
b=int (input("klavyeden 'b' degerini giriniz:"))
c=int (input("klavyeden 'c' degerini giriniz:"))


#diskriminant hesabı
d=(b**2)-(4*a*c)

coz1=(-b-cmath.sqrt(d))/(2*a)
coz2=(-b+cmath.sqrt(d))/(2*a)

print("1.cozum:{} ,2.cozum:{})".format(coz1,coz2))

