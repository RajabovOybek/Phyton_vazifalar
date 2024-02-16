# 07 dars List(ro'yxat)  topshiriqlari 
# sana: 07/02/2024
# muallif: Rajabov Oybek

#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 

ismlar = ["Umid", "Sirojiddin", "Karimboy"]
print (f"Salom {ismlar[0]} qalaysan?? \nBugun ob-xavo yaxshi-a {ismlar[1]}?? \nFutbol ko'ramizmi {ismlar[2]}??")

#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
#ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 

sonlar = [23, 8, -15, 99.9, -0.01]
print (f"bo'linma= {float(sonlar[3])/float(sonlar[4])}")
print (f"ko'paytma= {float(sonlar[2])*float(sonlar[3])}")
sonlar[1] = 100
del sonlar[0]
print(sonlar)

#t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi 
#tirik bo'lgan shaxslarning ismini kiriting. Ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()),
 
t_shaxslar = ["Imom al-Buxoriy", "al-Xorazmiy", "Ibn Sino", "al-Farg'oniy", "Dicaprio"]
z_shaxslar = ["Elon Musk", "Leo Messi", "Crishtiano Ronaldo", "Stiv Jobs", "Bil Gates"]
print (f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan, \nZamonaviy shaxslardan {z_shaxslar.pop(1)} bilan \nsuxbatlashishni xoxlardim")

#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.

friends = []
friends.append("Umid")
friends.append("Sirojiddin")
friends.append("Sherzod")
friends.append("Axror")
friends.append("Ibrat og'a")
friends.append("Zafar")
print (friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.

friends.remove("Zafar")
friends.remove("Ibrat og'a")
print (friends)

#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

friends.append("Asad")
friends.insert(0, "Toxir")
friends.insert(3, "Jasur")
print (friends)

#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga 
#kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

mexmonlar = []
mexmonlar.append(friends.pop(1))
mexmonlar.append(friends.pop(1))
mexmonlar.append(friends.pop(2))
print (f"Kelgan mexmonlar \n{mexmonlar}")