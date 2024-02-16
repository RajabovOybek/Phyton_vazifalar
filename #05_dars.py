# 05 dars string(MATN)  topshiriqlari 
# sana: 05/02/2024
# muallif: Rajabov Oybek

#Quyidagi o'zgaruvchilarni yarating: 
#kocha="Bog'bon"
#mahalla="Sog'bon"
#tuman="Bodomzor" 
#viloyat="Samarqand"
#Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
#Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"
print (f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

#Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini 
#foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.

kocha = input("ko'changizni kiriting=")
mahalla = input("mahallangizni kiriting=")
tuman = input("tumaningizni kiriting=")
viloyat = input("Viloyatingizni kiriting=")
print (f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

#Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing

print (f"{kocha} ko'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat} viloyati")

#Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
#manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.

yangi_manzil = f"{kocha.upper()} ko'chasi, \n{mahalla.lower()} mahallasi, \n{tuman.title()} tumani, \n{viloyat.capitalize()} viloyati"
print (yangi_manzil)

