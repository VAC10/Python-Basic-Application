# -*- coding: utf-8 -*-
"""
sayi=int(input("lutfen klavyeden sayi giriniz:"))
asal=True
for i in range(2,int(sayi)):
    if sayi%i==0:
        asal=False
        print("sayi asal degildir")
        break
    
    else:
        asal=True
        print("girdiginiz sayi asal sayidir")
        break
    """

def faktoriyel_hesapla(sayi):
    toplam=1
    for i in range(1,sayi+1):
        toplam=i*toplam
    print(f"{sayi} sayisinin faktoriyeli:",toplam)    
         
      

faktoriyel_hesapla(5)
    
sayi=int(input("klavyeden sayi giriniz:"))
toplam=1
i=0
while i<sayi:
    i+=1
    toplam=i*toplam
   # print(f"{i} sayisinin  faktoriyeli:",toplam)
    
print(f"{sayi} sayisinin  faktoriyeli:",toplam)
 
    
    
      













