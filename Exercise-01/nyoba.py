jumlahpembelanjaan = int(input("Masukkan jumlah pembelanjaan Anda = "))
member = input("apakah anda memiliki kartu member? iya/tidak=")
if member == "iya":
    if jumlahpembelanjaan>500000:
        disc = jumlahpembelanjaan*25/100
        print("Selamat Anda mendapatkan disc 25%")
        totalpembayaran=jumlahpembelanjaan-disc
        print("jumlah pembayaran Anda sebesar",int(totalpembayaran))
    elif jumlahpembelanjaan>100000 :
        disc = jumlahpembelanjaan*20/100
        print("Selamat Anda mendapatkan disc 20%")
        totalpembayaran=jumlahpembelanjaan-disc
        print("jumlah pembayaran Anda sebesar",int(totalpembayaran))
    else :
        disc = jumlahpembelanjaan*10/100
        print("Selamat Anda mendapatkan disc 10%")
        totalpembayaran=jumlahpembelanjaan-disc
        print("jumlah pembayaran Anda sebesar",int(totalpembayaran))
else:
    if jumlahpembelanjaan>100000:
        disc = jumlahpembelanjaan*10/100
        print("Selamat Anda mendapatkan disc 10%")
        totalpembayaran=jumlahpembelanjaan-disc
        print("jumlah pembayaran Anda sebesar",int(totalpembayaran))
    else:
         print("jumlah pembayaran Anda adalah",jumlahpembelanjaan)