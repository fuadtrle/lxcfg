import random
import datetime

#Dzžina (4 salt +):
duzinapw = 4

#koliko passworda:
kol = 10

#Koje karakteri se koriste za password. Izbačeni slični kao 0 i O, 1 i l 
UPPERc = 'ACDEFGHJKMNPQRTUVWX'
lowerC = 'abcdefghjkmnpqrtuvwx'
nummc = '2345679'
specC = '!*#=$%'
mixchargr = UPPERc + lowerC + nummc + specC

#Fajl u koji se upisuje lista
imefajla = "list_" + str(kol) + "_"
imefajla += str(datetime.datetime.now().day)
imefajla += str(datetime.datetime.now().month)
imefajla += str(datetime.datetime.now().year) + "."
imefajla += str(datetime.datetime.now().hour)
imefajla += str(datetime.datetime.now().minute)
imefajla += str(datetime.datetime.now().second)
imefajla += ".txt"
f = open(imefajla, "a")

def genpw():
	#pw_salt ispunjava uslov minimalno 1 veliko slovo, malo slovo, broj i specialni karakter
	#prvo veliko slovo zbog kopiranja u Word...
	pw_salt = random.choice(UPPERc) + random.choice(lowerC) + random.choice(nummc) + random.choice(specC)

	for p in range(duzinapw):
		pw_salt += random.choice(mixchargr)
	
	print(pw_salt)
	return str(pw_salt)
	#f.write(pw_salt)


for x in range(kol):
	f.write(genpw())
	if x < kol-1:
		#izbiti prazan red na kraju
		f.write("\n")

#zatvori fajl
f.close()
