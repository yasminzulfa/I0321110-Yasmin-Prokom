jumlahpembelanjaan=int(input("masukkan jumlah pembelanjaan anda = "))
member=input("apakah anda memiliki kartu member? iya atau tidak = ")
if member == "iya":
    if jumlahpembelanjaan>500000:
        print("selamat Anda mendapatkan disc 25%")
        totalpembayaran = jumlahpembelanjaan-(jumlahpembelanjaan*25/100)
    elif jumlahpembelanjaan>100000:
        print("selamat Anda mendapatkan disc 20%")
        totalpembayaran = jumlahpembelanjaan-(jumlahpembelanjaan*20/100)
    else :
        print("selamat Anda mendapatkan disc 10%")
        totalpembayaran = jumlahpembelanjaan-(jumlahpembelanjaan*10/100)
else:
    if jumlahpembelanjaan>100000:
        print("selamat Anda mendapatkan disc 10%")
        totalpembayaran = jumlahpembelanjaan-(jumlahpembelanjaan*10/100)
    else:
        print("Mohon maaf Anda tidak mendapatkan disc")
        totalpembayaran = jumlahpembelanjaan

print("Jumlah pembayaran Anda sebesar", jumlahpembelanjaan)