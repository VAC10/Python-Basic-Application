# -*- coding: utf-8 -*-
#kilo degerini bulduran program
"""
kilo=int(input("lutfen kilonuzu giriniz:"))

if kilo<=60:
    print("zayıfsınız")
elif kilo>=80:
    print("kilolusunuz")
    
elif 50<kilo<80:
    print("Fitsin")"""
"""
#asal sayi bulma
sayac=0
sayi=int(input("lutfen bir sayi giriniz:"))

for i in range (2,int(sayi)):
    if(int(sayi)%i==0):
        sayac+=1
        break
if (sayac!=0):
    print("girilen sayi asal deil")
    
else:
    print("girilen sayi asaldir.")
     
#asal sayı bulma başka versiyon
sayi=int(input("sayi girin:"))
asal=1

for i in range(2,int(sayi)):
    if sayi%i==0:
         asal=0
         print("sayi asal deil")  
         break        
    else: 
        asal=1
        print("sayi asal asaldır")   
        break"""
#dikdörtgenin alanını fonksiyonla hesaplama
"""
def alanhesapla(kısa,uzun):
    alan=kısa*uzun
    print("alan:",alan)
    return alan

kısa=float(input("kısa kenarı giriniz:"))
uzun=float(input("uzun kenarı giriniz:"))

alanhesapla(kısa,uzun)"""
# baslangıc ve bitis degeri girilen iki sayı arasındaki cift sayıların ortalaması
"""
toplam=0
sayac=0
baslangıc=int(input("klavyeden baslangıc degeri giriniz:"))
bitis=int(input("klavyeden bitis degeri giriniz:"))
for sayilar in range(baslangıc,bitis+1):
    if sayilar%2==0:
        toplam=toplam+sayilar
        sayac+=1
   
        
print(f"{baslangıc} sayisi ile {bitis} sayiları arasındakı cıft sayilarin ortalamasi=",toplam/sayac)
"""   
#yazi tura örnegi
"""   
import random
liste=["yazi","tura"]
a=random.choice(liste)
yazi=liste[0]
tura=liste[1]
deger=str(input("yazımı turamı?:"))


if deger==yazi:
    if a==yazi: 
        print("tahminin dogru")
        
           
    else: 
        print("tahminin yanlıs")

if deger==tura:
    if a==tura:
        
        print("tahminin dogru")
      
    else:
        print("tahminin yanlıs")
"""
#sesli harfi bulma
"""
sayac=1
metin=str(input("lutfen bir metin giriniz:"))
sesliharfler={"a","ı","o","ö","ü","u","e"}

for i in metin:
    if i in sesliharfler:
        sayac+=1
        
print("sesli harfler:",sayac)"""
"""
#girilen 10 adet sayıdan en buyugunu bulan program
liste=[]
def enbuyuksayi(liste): 
    for i in range(10):
        sayilar=int(input(f"lutfen klavyeden {i+1}. sayi giriniz:")) 
        liste.append(sayilar)
        liste.sort()
        #liste.reverse() #buyukten kucuge sıraladık
    #print("girilen en buyuk sayi:",liste[0])
    print("girilen en buyuk sayi:",max (liste))
 
       
enbuyuksayi(liste)  """ 
"""         
#girilen 10 adet sayıdan en kucugunu bulan program
liste=[]
def enkucukbul (liste):
    for i in range(5):
        sayilar=int(input(f"lutfen {i+1}.sayiyi giriniz:"))
        liste.append(sayilar)
    print("en kucuk sayi:",min(liste))


enkucukbul(liste)"""            
            

























































        