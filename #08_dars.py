# 08 dars ro'yxatlar bilan ishlash  topshiriqlari 
# sana: 08/02/2024
# muallif: Rajabov Oybek

#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring

country = ["Braziliya", "O'zbekiston", "AQSH", "Argentina", "Germaniya", "Britaniya"]
print (country)

#Ro'yxatning uzunligini konsolga chiqaring

print (len(country))

#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring

print (sorted(country))

#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

print (sorted(country, reverse=True))

#Asl ro'yxatni qaytadan konsolga chiqaring

print (country)

#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring

country.reverse()
print(country)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.

country.sort()
print (country)
country.sort(reverse=1)
print (country)

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing

j_sonlar = list(range(120,1200, 2))
print (j_sonlar)

#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring

print (sum(j_sonlar))

#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring

print (max(j_sonlar)-min(j_sonlar))

#Ro'yxatdagi elementlar sonini hisoblang

print (len(j_sonlar))

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

print (j_sonlar[0:21])
print (j_sonlar[260:280])
print (j_sonlar[-21:-1])

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting

taomlar = ["palov", "shutoshi", "manti", "somsa", "shashlik"]

#nonushta degan yangi ro'yxatga taomlardan nusxa oling

nonushta = taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing

nonushta.remove("shutoshi")
nonushta.remove("manti")
del nonushta [2]
nonushta.append("sariyog' non")
nonushta.append("tuxum")

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring

print (taomlar)
print (nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.

nonushta = tuple(nonushta)
#o'zgarmas ro'yxat qildik shuning uchun ham xatolik beradi
nonushta[0]="qaymoq va non"