cariNim = input('Masukkan NIM yang dicari :')
file = open('Data2.txt', 'r')
a = file.readlines()

for i in range(len(a)) :
    if(cariNim in a[i]) :
        keterangan = 'ada'
        break
    else :
        keterangan = 'tidak ada'
        continue
if(keterangan == 'ada') :
        b = a[i].split('|')
        print('\nData Mahasiswa')
        print('NIM    :', b[0])
        print('Nama   :', b[1])
        print('Alamat :', b[2])
else :
    print('Data mahasiswa tidak ditemukan')
