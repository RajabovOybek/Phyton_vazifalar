# 11 dars if-else  topshiriqlari 
# sana: 11/02/2024
# muallif: Rajabov Oybek

#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!",
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

juft_son = int(input("Juft son kiriting>>>>"))
if juft_son % 2==0:
    print ("Raxmat")
else:
    print ("Bu juft son emas")

#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
    
yosh = int(input("yoshingiz nechada?>>>"))
if yosh<=4 or yosh>=60:
    print ("Siz uchun bepul")
elif yosh<18:
    print ("Siz uchun 10_000 so'm")
elif yosh >=18:
    print ("Siz uchun 20_000 so'm")

#Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularni teng yoki katta/kichikligi haqida xabarni chiqaring

son_1 = float(input("1-sonni kiriting>>>>"))
son_2 = float(input("2-sonni kiriting>>>>"))
if son_1>son_2:
    print (f"{son_1} > {son_2}")
elif son_2>son_1:
    print (f"{son_1} < {son_2}")
else:
    print (f"{son_1} = {son_2}")

#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan 
#savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni,mahsulotlar ro'yxati bilan solishtiring va qaysi biri 
#ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
    
maxsulotlar = ["laptop", "pc", "telefon", "kalonka", "klava", "mishka", "monitor", "kreslo", "led lampa", "sumka"]
savat = []
n = int(input("nechta maxsulot olmoqchisiz>>>>"))
if n>0 or n<11:
    for n in range(0,n):
        savat.append(input(f"{n+1}-maxsulotni kiriting\n"))
    print (savat)
    for maxsulot in savat:
        if maxsulot in maxsulotlar:
            print ("Do'konimizda", maxsulot, "bor")
        else:
            print("Do'konda", maxsulot, "yo'q")
else:
    print ("Maxsulot tanlang")

#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan n ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi, 
#bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, 
#"Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

maxsulotlar = ["laptop", "pc", "telefon", "kalonka", "klava", "mishka", "monitor", "kreslo", "led lampa", "sumka"]
savat = []
bor_mahsulotlar = []
mavjud_emas = []
n = int(input("nechta maxsulot olmoqchisiz>>>>"))

if n>0 and n<11:

    for n in range(0,n):
        savat.append(input(f"{n+1}-maxsulotni kiriting\n"))
    print (savat)

    for maxsulot in savat:

        if maxsulot in maxsulotlar:
            bor_mahsulotlar.append(maxsulot)
            print ("Do'konimizda", maxsulot, "bor")

        else:
            mavjud_emas.append(maxsulot)
            print("Do'konda", maxsulot, "yo'q")

    print ("bor mahsulotlar", bor_mahsulotlar)

    if len(mavjud_emas)==0:
        print ("Siz so'ragan barcha maxsulot bor")
    
    else:
        print ("quyidagi narsalar do'konda yo'q", mavjud_emas)

elif n>=11:
    print ("Do'konda buncha maxsulot yo'q")

elif n<=0:
    print ("Xato malumot kiritdingiz \ndasturni qaytadan ishlating")

#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login yozishni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning 
#tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

foydalanuvchilar = ["Oybek", "Rajabov", "matematika", "UrDU", "222-guruh"]
login = input("login yozing\n")
if login in foydalanuvchilar:
    print ("Login band, yangi login tanlang!")
else:
    print ("Xush kelibsiz,", login)

#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

son = int(input("Istalgan butun son kiriting>>>>"))
for n in range(1,11):
    if son % n ==0:
        print (f"{son} soni {n} ga qoldiqsiz bo'linadi")
    #else:
        #print (f"{son} soni {n} ga bo'linmaydi")
