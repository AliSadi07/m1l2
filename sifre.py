import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre_uzunlugu = int(input("Şifrenin uzunluğunu girin: "))


sifre = ""

if sifre_uzunlugu >= 8:
    for i in range(sifre_uzunlugu):
        sifre = sifre + random.choice(karakterler)
else:
    print("Şifre uzunluğunuz en az 8 olabilir")
print(sifre)
