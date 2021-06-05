# -*- coding: utf-8 -*-
#Basit Hesap makinesi
def toplama(x,y):
    return x+y

def cikarma (x,y):
    return x-y

def bolme (x,y):
    return x/y

def carpma (x,y):
    return x*y


print("Lutfen asagida belirtilen islem numarlarından birini seciniz")

print("1-Toplama")
print("2-Cikarma")
print("3-Carpma")
print("4-Bolme")
    
while True:
    secim=input("lutfen seciminizi yapiniz(1/2/3/4):")
    if secim in("1","2","3","4"):
        num1=float(input("lutfen birinci sayiyi giriniz:"))
        num2=float(input("lutfen ikinci sayiyi giriniz:"))
        
        
        if secim=='1':
            print("isleminizin sonucu:",toplama(num1, num2))
            
        elif secim=='2':
            print("isleminizin sonucu:",cikarma(num1, num2))    
            
        elif secim=='3':
            print("isleminizin sonucu:",carpma(num1, num2))    
        elif secim=='4':
            print("isleminizin sonucu:",bolme(num1, num2))  
        break   
            
    else:
            print("yalnıs deger")
            
            
            