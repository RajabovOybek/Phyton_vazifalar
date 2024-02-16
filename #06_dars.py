# 06 dars sonlar  topshiriqlari 
# sana: 06/02/2024
# muallif: Rajabov Oybek

#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur

a = float(input("Istalgan butun son kiriting= "))
print (f"{a} ning kvadrati= {a**2}")
print (f"{a} ning kubi= {a**3}")

#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur

yosh = int(input("Yoshingiz nechada?>>>"))
print (f"Siz {2024-yosh} yilda tug'ilgansiz")

#Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

a = float(input("1-sonni kiriting= "))
b = float(input("2-sonni kiriting= "))
print (f"Yig'indisi= {a+b}")
print (f"Ayirmasi= {a-b}")
print (f"Ko'paytmasi= {a*b}")
print (f"Bo'linmasi= {a/b}")