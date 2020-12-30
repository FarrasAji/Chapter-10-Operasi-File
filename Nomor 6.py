def encrypt(teks, n) :
    daftarteks = list(teks)
    for x in range(len(daftarteks)) :
        if(daftarteks[x] != ' ') :
            if(ord(daftarteks[x]) + n < 90) :
                asciiCode = ord(daftarteks[x])
                encrypted = asciiCode + n
                daftarteks[x] = chr(encrypted)
            else :
                asciiCode = ord(daftarteks[x])
                encrypted = (asciiCode + n) - 26
                daftarteks[x] = chr(encrypted)
        else :
            continue
    result = ''.join(daftarteks)
    return result
try :
    teks = input("Masukkan teks yang akan dienkripsi : ")
    n = int(input("Masukkan jumlah geseran enkripsi : "))
    hasilenkripsi = encrypt(teks, n)
    print("Hasil pengenkripsian teks {0} adalah : {1}".format(teks, hasilenkripsi))
except ValueError :
    print("Masukkan bilangan bulat")
