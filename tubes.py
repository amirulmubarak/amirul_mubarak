import re
import random
#fungsi,perulangan,kondisi,erorhandling,GUI/visualisasi
print("Selamat datang, ketik 'Halo' untuk memulai interaksi dengan kami")
def menu_motor():
    print(''''
    ===> SELAMAT DATANG DI RENTAL MOTOR AGUS<===
    SILAHKAN PILIH MENU BERIKUT:
    1. Vario
    2. Aerok
    3. Beat Mberr
    4. RX King''')
    pilih = input("Pilihan : ")
    if pilih == 1 :
        print("Ok silahkan ambil sekarang di jl. batununggal")
    elif pilih == 2:
        print("Ok silahkan ambil sekarang di jl. batununggal")
    elif pilih == 3:
        print("Ok silahkan ambil sekarang di jl. batununggal")
    elif pilih == 4:
        print("Ok silahkan ambil sekarang di jl. batununggal")
balasan_bot = ["Selamat datang di Rental Motor Pak Joko, Ada yang bisa kami Bantu? (Katakan 'ya' untuk melanjutkan)"]

while True:
    x = (input("user\t: "))
    if re.findall(r"halo|Halo", x):
        print("bot\t:", random.choice(balasan_bot))
    else:
        print("Coba mulai dengan 'ya'")
        try :
            y = input("user: ")
            if y == "ya" or y == "Ya":
                menu_motor()
                            
        except ValueError:
            print("Program ini hanya menerima respon berupa 'Ya'")

    


