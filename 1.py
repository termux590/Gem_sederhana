import random
posisi_saya=random.randint(1,4)

soal_pertama =random.randint(1,100)
soal_kedua =random.randint(1,100)

soal_pertama_kurang =random.randint(1,100)
soal_kedua_kurang =random.randint(1,100)                              
soal_pertama_kali =random.randint(1,100)
soal_kedua_kali =random.randint(1,100)

soal_pertama_bagi =random.randint(1,100)
soal_kedua_bagi =random.randint(1,100)

soal_pertama_pangkat =random.randint(1,100)                           soal_kedua_pangkat =random.randint(1,100)

jawabanya_adalah =float(soal_pertama + soal_kedua)
jawabanya_adalah_dua = soal_pertama - soal_kedua                      jawabanya_adalah_tiga = soal_pertama * soal_kedua
jawabanya_adalah_empat = soal_pertama / soal_kedua
jawabanya_adalah_lima = soal_pertama ** soal_kedua

print('''
********************************
 *****welcome to gem tim*****
********************************
''')
user =input("masukan nama anda:")
pw =input("masukan katasandi anda: ")


if pw =="123":
   print(f'''
************************
** nama = {user}
** pw   = {pw}
** katasandi = benar ✅
************************
''')
else:
  print("maaf kata sandi yang ada masukin salah",pw)
  exit()
print('''
____________________________________________
|pencipta = RIZYAN PADILAH                 |
|IG = https://www.instagram.com/tskyz_stars|
|WA =+62882019175896                       |
____________________________________________
***************
*1.KALULATOR  *
*2.GEM        *
*3.EXIT       *
***************
''')

opsi =input("masukan pilihan:")
if opsi =="3":
   print("goodbyee",user)
   exit()
if opsi =="2":
   print(f'''
   ************************
   *** Gem Tebak-Tebakan***
   ************************''')
   gem =input(f''' |__| |__| |__| |__| TEMUKAN DI MANA KH SAYA BERADA (1/2/3/4):''')                                                           if gem ==posisi_saya:
      print("kamu menemukan saya di goa",gem)
   elif gem !="1" or "2" or "3" or "4":
     print("masukin yang beber gk ada goa",gem)
     exit()
   else:
     print("saya bukan di goa",gem,"tapi saya berada goa",posisi_saya)
     exit()
if opsi =="1":
   print('''
*****kalkulator*********
*1.+
*2.-
*3.x
*4./
*5.**
*6.pertanyaan acak
*7.keluar
*******************
''')
else:
  print("masukin yang bener")
  exit()

opsi_kalkulator =input("pilih opsi:")
if opsi_kalkulator =="1" and "2" and "3" and "4" and "5":
   lanjut =input("kamu yakin lanjut?(y/n):")
   if lanjut =="y":
      y =float(input("masukin angka pertama:"))
      x =float(input("masukin angka kedua :"))
      if opsi_kalkulator =="1":
         print(f'''pertanyaaan anda {y} + {x} = {y+x}''' )
         exit()
      if opsi_kalkulator =="2":
         print(f'''pertanyaaan anda {y} - {x} = {y-x}''' )
         exit()
      if opsi_kalkulator =="3":
         print(f'''pertanyaaan anda {y} × {x} = {y*x}''' )
         exit()
      if opsi_kalkulator =="4":
         print(f'''pertanyaaan anda {y} / {x} = {y/x}''' )
         exit()
      if opsi_kalkulator =="5":
         print(f'''pertanyaaan anda {y} ** {x} = {y**x}''' )
         exit()

if opsi_kalkulator =="7":
   print("goodbye",user)
   exit()


if opsi_kalkulator =="6":
    print(f'''
**************************                                             ****pilihpertanyaaan****
*1.+
*2.-
*3.x
*4./
"5.**
*6.exit ''')
opsi_pertanyaan =input("masukan pilihan:")
if opsi_pertanyaan =="1":                                                print(f''' {soal_pertama} + {soal_kedua} = ?''' )
   jawaban =float(input("berapa kah jawabannya:"))
if opsi_pertanyaan =="2":
   print(f''' {soal_pertama_kurang} - {soal_kedua_kurang} = ?''' )
   jawaban_dua =float(input("berapa kah jawabannya:"))
if opsi_pertanyaan =="3":
   print(f''' {soal_pertama_kali} × {soal_kedua_kali} = ?''' )
   jawaban_tiga =float(input("berapa kah jawabannya:"))
if opsi_pertanyaan =="4":
   print(f''' {soal_pertama_bagi} / {soal_kedua_bagi} = ?''' )
   jawaban_empat =float(input("berapa kah jawabannya:"))
if opsi_pertanyaan =="5":
   print(f''' {soal_pertama_pangkat} ** {soal_kedua_pangkat} = ?''' )
   jawaban_lima =float(input("berapa kah jawabannya:"))




if jawaban ==jawabanya_adalah:
   print("jawaban anda benar selamat")
   exit()
if jawaban_dua ==jawabanya_adalah_dua:
   print("jawaban anda benar selamat")
   exit()
if jawaban_tiga ==jawabanya_adalah_tiga:
   print("jawaban anda benar selamat")
   exit()
if jawaban_empat ==jawabanya_adalah_empat:
   print("jawaban anda benar selamat")
   exit()
if jawaban_lima ==jawabanya_adalah_lima:
   print("jawaban anda benar selamat")
   exit()

else:
  print("dongo gitu doang gk bisa")
  exit()