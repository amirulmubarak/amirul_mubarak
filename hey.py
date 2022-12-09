'''bulan=int(input("Masukkan nomor bulan : "))
if bulan==1:
    print("Bulan ke-1 adalah Januari")
elif bulan==2:
    print("Bulan ke-2 adalah Februari")
elif bulan==3:
    print("Bulan ke-3 adalah maret")
elif bulan==4:
    print("Bulan ke-4 adalah april")
elif bulan==5:
    print("Bulan ke-5 adalah mei")
elif bulan==6:
    print("Bulan ke-6 adalah juni")
elif bulan==7:
    print("Bulan ke-7 adalah juli")
elif bulan==8:
    print("Bulan ke-8 adalah agustus")
elif bulan==9:
    print("Bulan ke-9 adalah september")
elif bulan==10:
    print("Bulan ke-10 adalah oktober")
elif bulan==11:
    print("Bulan ke-11 adalah november")
elif bulan==12:
    print("Bulan ke-12 adalah desember")
else:
    print("Maaf tapi penomoran bulan hanya sampai 12 ya")'''

#nomor 2
'''a=int(input("Masukkan bilangan pertama : "))
x=input("Masukkan operasinya: ")
b=int(input("Masukkan bilangan kedua: "))
match x:
    case "+":
        print("Hasilnya adalah= ",a+b)
    case "-":
        print("Hasilnya adalah= ", a-b)
    case _:
        print("Kalkulator ini hanya bisa menghitung penjumlahan dan pengurangan ya bosku")'''


'''angka = [1,2,3,4,5,30]
def genapnya(aSequence):
    for x in angka:
        if x%2 == 0:
            print(x, "adalah genap")
def maksimum(aSequence):
    for x in angka:
        if x == max(angka):
            print(x, "adalah max")
def rata_rata(aSequence):
    for x in angka:
        if x == 1:
            y = float((sum(angka))/len(angka))
            print(y, "adalah rata-rata")

genapnya(angka)
maksimum(angka)
rata_rata(angka)'''

'''from re import X


list1 = ["asmuni", "jujuk","tarzan","bon jovi","mark"]
def secondChar(string1):
    for x in list1:
        
        print(x[2])
secondChar(list1)'''

from tkinter import *
import tkinter.font

main = Tk(className=" ")
main.geometry("500x600")
change_font = tkinter.font.Font(size=10)
kop = Label(main,text="FORM PEMESANAN THE RENTALS", foreground="green", font=change_font).place(x=120, y=10)
hasil = LabelFrame(main, text="Detail Pesanan")
hasil.place(x = 150, y= 350)


nama = Label(main, text="Masukkan nama lengkap (sesuai KTP)").place(x=20, y=50)
wa = Label(main, text="Masukkan nomor Whatsapp").place(x=20, y=90)
ins = Label(main, text="Masukkan nama akun instagram (tanpa @)").place(x=20, y=130)
gender = Label(main, text="Pilih Jenis Kelamin").place(x=20, y=170)
vehicle = Label(main, text="Pilih Jenis motor").place(x=20, y=210)
paket = Label(main, text="Pilih paket").place(x=20, y=250)

d0 = Entry(main, width=40)
d1 = Entry(main, width=40)
d2 = Entry(main, width=40)

d0.place(x=20, y=70)
d1.place(x=20, y=110)
d2.place(x=20, y=150)

s = StringVar()
s.set("Pria")
#opsi gender
gend = Radiobutton(main, text="Pria",variable=s, value="Pria").place(x=20, y=190)
gend2 = Radiobutton(main, text="Wanita",variable=s,value="Wanita").place(x=80, y=190)
#opsi motor
t = StringVar()
t.set("Vario")
moto1 = Radiobutton(main, text="Vario",variable=t, value="Vario").place(x=20, y=230)
moto2 = Radiobutton(main, text="Beat",variable=t, value="Beat").place(x=80, y=230)
moto3 = Radiobutton(main, text="Mio",variable=t, value="Mio").place(x=140, y=230)
#opsi paket
p = StringVar()
p.set("Setengah hari")
paket1 = Radiobutton(main,text="Setengah hari", variable=p,value="Setengah hari").place(x=20, y=270)
paket2 = Radiobutton(main,text="Satu hari", variable=p,value="Satu hari").place(x=120, y=270)
paket3 = Radiobutton(main,text="Empat hari", variable=p,value="Empat hari").place(x=220, y=270)
paket4 = Radiobutton(main,text="Satu minggu", variable=p,value="Satu minggu").place(x=320, y=270)

def confirm():
    Label_confirm = Label(main, text="Pesananmu telah diproses! motor akan diantar dalam 30 menit\n info : kwitansi dan info lainnya dikirim melalui Whatsapp", foreground="green").place(x=100, y=480)
def pesan():
    class pemesan :
        def __init__(self, nama, wa, ins, gender, vehicle, paket):
            self.nama = nama
            self.wa = wa
            self.ins = ins
            self.gender = gender
            self.vehicle = vehicle
            self.paket = paket
        def pesanan(self):
            hasil_pesan = Label(hasil, text="Nama : "+self.nama+"\n Nomor Wa : "
            +self.wa+"\n Akun Instagram : "+self.ins+"\n Jenis Kelamin : "+self.gender+
            "\n Motor : "+self.vehicle+"\n Paket : "+self.paket).grid()
    show = pemesan(d0.get(), d1.get(), d2.get(), s.get(), t.get(), p.get())
    show.pesanan()
    konfirmasi = Button(main, text="Konfirmasi Pesanan", activebackground="blue", command=confirm).place(x=280, y=450)

button = Button(main, text = "Pesan", command= pesan).place(x=200, y=310)


main.mainloop()