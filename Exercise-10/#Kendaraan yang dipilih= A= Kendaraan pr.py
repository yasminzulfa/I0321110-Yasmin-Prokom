#Kendaraan yang dipilih= A= Kendaraan pribadi, B= Bus, C= Truk
#Tanggal= Jika H-1 diisi dengan 1 dan H-6 diisi dengan 6
print("====")
print(" ")
print("Welcome To Pintu Gerbang Tol Surakarta")
Jarak= int(input('Jarak yang telah ditempuh: '))
Tanggal= int(input("Kapan kamu akan tiba [jarak dengan lebaran]: "))
Kendaraan = input("Kendaraan yang digunakan:")
if Tanggal <= 5 : 
    if Kendaraan == "A" :
        print("Total Harga Tarif Pembayaran Anda adalah: " , Jarak * (0.8*1000))
    elif Kendaraan == "B" :
        print("Total Harga Tarif Pembayaran Anda adalah: " , Jarak * (0.8*1500))
    else:
        print("Total Harga Tarif Pembayaran Anda adalah: " , Jarak * (0.8*2000))
else:
    if Kendaraan == "A" :
        print("Total Harga Tarif Pembayaran Anda adalah: " , Jarak *1000)
    elif Kendaraan == "B" :
        print("Total Harga Tarif Pembayaran Anda adalah: " , Jarak *1500)
    else:
        print("Total Harga Tarif Pembayaran Anda adalah: " , Jarak *2000)
