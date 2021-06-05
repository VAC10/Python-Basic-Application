# -*- coding: utf-8 -*-
#yıldızla ucgen olusturma.
"""
rows=int(input("lutfen satir sayisini giriniz:"))

for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    
    print("\n")    """
#sayilarla sıralı şekilde üçgen oluşturma.    
"""
satir = int(input("satir sayisini giriniz: "))

for i in range(satir):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")   """ 
 #yıldızlarla piramit oluşturma

satir=int(input("satir sayisi gir:"))
k=0

for i in range(1,satir+1):  
    for bosluk in range(1,(satir-i)+1):
        print(end="  ")
        
    while k!=(2*i-1):
        print("* ", end="")
        k+=1
        
    k=0
    print( )        