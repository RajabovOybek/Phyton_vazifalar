# 10 dars if-else  topshiriqlari 
# sana: 10/02/2024
# muallif: Rajabov Oybek

#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining 
#birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == "gm":
        print (car.upper())
    else:
        print (car.title())

#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != "gm":
        print (car.title())
    else:
        print (car.upper())

#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" 
#xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.

login =input("Loginni kiriting\n") 
if login.lower == "admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print ("Xush kelibsiz,", login)

#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

son_1 = float(input("1-sonni kiriting>>>")) 
son_2 = float(input("2-sonni kiriting>>>")) 
if son_1 == son_2:
    print (f"Sonlar teng, {son_1}={son_2}")

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 

son = float(input("Istalgan son kiriting>>>>"))
if son >= 0:
    print ("Musbat son")
else:
    print ("Manfiy son")

#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 

son = float(input("Istalgan son kiriting>>>>"))
if son >= 0:
    print ("Sonning ildizi", son**(1/2), "ga teng")
else:
    print ("Musbat son kiriting")