def biodata (tahunLahir, Nama, Asal):
    tahun_sekarang = 2020
    print(f'\nPerkenalkan Nama Saya : {Nama}')
    print(f'Umur Saya : {tahun_sekarang - tahunLahir}')
    print(f'Saya Adalah Angkatan : {tahun_sekarang}')
    return(f'Asal Saya : {Asal}')

for i in range(2):
    tahunLahir = int(input())
    Nama = input()
    Asal = input()
    print(biodata(tahunLahir, Nama, Asal))

