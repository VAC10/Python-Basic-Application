# -*- coding: utf-8 -*-
asimHesap= {
    'ad':'asım',
    'hesapNo': '1234567',
    'bakiye':4000,
    'ekhesap':2000
    }

semihHesap={
    'ad':'semih',
    'hesapNo':'654321', 
    'bakiye':6000,
    'ekhesap':3000
    }

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    
    if(hesap['bakiye'])>=miktar:
        hesap['bakiye']=hesap['bakiye']-miktar
        print("paranızı alabilirsiniz.")
       # bakiyeSorgula(hesap)
    else:
        toplam= hesap['bakiye']+hesap['ekhesap']
        
        if (toplam>=miktar):
           
            ekhesapkullanimi=input("ekhesap kullanılsın mı? (e/h)")
            
            if(ekhesapkullanimi=='e'):
                 ekhesapkullanilcakMiktar=miktar- hesap['bakiye']
                 hesap['bakiye']=0
                 hesap['ekhesap']-=ekhesapkullanilcakMiktar
                 print("paranizi alabilrsiniz.")
                # bakiyeSorgula(hesap) 
                 
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir.")
        else:
            print("uzgunuz bakiye yetersiz..")
           # bakiyeSorgula(hesap)
  
    
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekhesap']} TL dir.")
    
    
paraCek(asimHesap,3000)
bakiyeSorgula(asimHesap) 
print("***********")
paraCek(asimHesap,2500) 
bakiyeSorgula(asimHesap)      
        
        
            
            
        
        
       
       

