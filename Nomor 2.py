file = open('Data2.txt','a')
status = True
while (status == True) :
    nim = input('Masukkan NIM Mahasiswa/i : ')
    namaMahasiswa = input('Masukkan Nama Mahasiswa/i : ')
    alamat = input('Alamat Mahasiswa/i  : ')
    file.write(nim + '|' + namaMahasiswa + '|' + alamat + '\n')  
    konfirmasi = input('Ingin input data lagi ? (y/n) : \n')
    
    if (konfirmasi == 'y') :
        status = True
    elif (konfirmasi == 'n') :
        status = False
        print('Data tersimpan')

file.close()
