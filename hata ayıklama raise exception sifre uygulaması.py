# -*- coding: utf-8 -*-
def check_password(psw):
    import re
    '''regular expression modulü; duzenli ifadeleri yakalamamız anlamına gelir.
             aşağıda yaptığımız işlemlerin kontorlunu sağlar ve search match gibi metodları vardır.
             '''
    if len(psw)<8:
        raise Exception("parola en az 7 karakterli olmalıdır.")
    elif not re.search("[a-z]",psw):
        raise Exception ("parola kucuk harf içermelidir.")
    elif not re.search("[A-Z]",psw):
        raise Exception ("parola buyuk harf içermelidir.")    
    elif not re.search("[0-9]",psw):
        raise Exception ("parola rakam içermelidir.") 
    elif not re.search("[_@*]",psw):
        raise Exception ("parola alpha numeric karakter içermelidir.") 
    elif re.search("\s",psw): #regulary expression'da bosluk, \s ile ifade edilir.
        raise Exception ("parola bosluk içermemelidir.")
    else: #try bloğunun içinde herhangi bir hata olmadığında else bloğu çalışır.
        print("Geçerli Parola!")
password=input("sifreyi giriniz:")    
    
try:
    check_password(password)
except Exception as ex:#exception 'genel bir hata' olursa yani diğer hatalarda ya da kestiremediğimiz hatalarda exception kullanılır
    print(ex) #exception genel hata tanımlaması en alta yapılmalı.
finally:
    print("valudiation(onaylama) tamamlandı.")# try except bloğu olumlu ya da olumsuzda olsa finaly çalışacak.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

