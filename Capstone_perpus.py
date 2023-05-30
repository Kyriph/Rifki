# Data
listPerpus = [['A001', 'Mengenal dinosaur', 'Andi', 'jl bambu', '13-11-2022'],
            ['B011', 'Mengenal angka', 'Budi', 'jl dusun', '13-11-2022'],
            ['B002', 'Mengenal data science', 'Cahyadi', 'jl bihun', '14-11-2022'],
            ['A003', 'Mengenal matematika', 'Dandi', 'jl mie', '15-11-2022']
            ]
    
# Tabel data
def data():
    print('Data Pinjaman Buku'.center(150,'='))
    for baris in range(len(listPerpus)):
        for kolom in range(1):
            if baris == 0 and kolom == 0:
                print('Kode Buku'.center(30), 'Nama Buku'.center(30), 'Nama Peminjam'.center(30), 'Alamat Peminjam'.center(30), 'Tanggal Peminjaman'.center(30))
                print('-'*150)

        for kolom in range(5):
            print(listPerpus[baris][kolom].center(30), end = ' ')

        print('')
    if len(listPerpus) == 0 :
        print('Data kosong, Mohon input data'.center(150,'='))
        
# Mencari listPerpus Kode buku
def kodeBuku():
    kode = input('Masukkan kode Buku: ').title()
    ketemu = False
    for baris in range(len(listPerpus)):
        if kode == listPerpus[baris][0]:
            dataBaru = baris
            for kolom in range(1):
                if kolom == 0:
                    print('Kode Buku'.center(30), 'Nama Buku'.center(30), 'Nama Peminjam'.center(30), 'Alamat Peminjam'.center(30), 'Tanggal Peminjaman'.center(30))
                    print('-'*150)

            for kolom in range(5):
                print(listPerpus[dataBaru][kolom].center(30), end = ' ')

            print('')
            ketemu = True
    if ketemu == False :
        print('Data tidak ditemukan'.center(90,'#'))
    

# mengecek primary key (Kode buku)
def mengecek(buku):    
    for baris in range(len(listPerpus)):
        if buku == listPerpus[baris][0]:
            return True
    return False

# mencari index primaty key (Kode buku)
def mengecekIndex(index):
    for baris in range(len(listPerpus)):
        if index == listPerpus[baris][0]:
            return baris

# sort berdasarkan kode buku
def sort():
    global listPerpus
    listSort = sorted(listPerpus, key = lambda l:l[0])
    listPerpus = listSort 
    data()

# Menampilkan data
def tampil():
    while True:
        print('Menu 1'.center(90,'='))
        print('1. Menampilkan seluruh data peminjaman buku')
        print('2. Menampilkan data untuk kode buku yang diinginkan')
        print('3. Kembali ke menu utama')

        pilihanMenu = input('Pilih Menu : ')
        if pilihanMenu == '1':
            data()

        elif pilihanMenu == '2':
            kodeBuku()
            
        elif pilihanMenu == '3':
            break

# Menambahkan data
def tambah():
     while True:
        print('Menu 2'.center(90,'='))
        print('1. Menambahkan data peminjaman buku')
        print('2. Kembali ke menu utama')

        pilihan = input('Pilih Menu : ')
        list_tambah =[]
        if pilihan == '1':
            print('Menu 2'.center(90,'='))
            buku = input('Masukkan kode buku: ').title()
            cek = mengecek(buku)
            if cek :
                print('Data sudah ada'.center(90,'#'))
            else:
                list_tambah.append(buku)
                nama = input('Masukkan nama buku: ').title()
                list_tambah.append(nama)
                peminjam = input('Masukkan nama peminjam: ').title()
                list_tambah.append(peminjam)
                alamat = input('Masukkan alamat peminjam: ').title()
                list_tambah.append(alamat)
                tanggal = input('Masukkan tanggal peminjaman: ').title()
                list_tambah.append(tanggal)
                for kolom in range(1):
                    if kolom == 0:
                        print('Kode Buku'.center(30), 'Nama Buku'.center(30), 'Nama Peminjam'.center(30), 'Alamat'.center(30), 'Tanggal Peminjaman'.center(30))
                        print('-'*150)

                for kolom in range(5):
                    print(list_tambah[kolom].center(30), end = ' ')

                pilihan = input('\nApakah anda ingin menambahkan data? y/t: ').lower()
                if pilihan == 'y':
                    listPerpus.append(list_tambah)
                    print(f'Data {buku} berhasil ditambahkan'.center(90,'-'))
                elif pilihan == 't':
                    print(f'Tambah data {buku} dibatalkan'.center(90,'#'))
                    tambah()
        elif pilihan == '2':
            break
        else:
            print('Masukkan Inputan yang benar'.center(90,'#'))

# Mengubah data
def mengubah():
    while True:
        print('Menu 3'.center(90,'='))
        print('1. Mengubah data peminjaman buku')
        print('2. Kembali ke menu')

        pilihan = input('Pilih Menu : ')
        if pilihan == '1':
            data()
            print('Menu 3'.center(90,'='))
            buku = input('Masukkan kode buku yang mau diubah: ').title()
            cek = mengecek(buku)
            indexBuku = mengecekIndex(buku)
            if cek :
                diubah = input('Masukkan kolom yang ingin diubah: ').title()
                match diubah :
                    case 'Nama Buku':
                        ubahBuku = input('Mengubah nama buku: ').title()
                        pilihan = input('\nApakah anda ingin mengubah data? y/t: ').lower()
                        if pilihan == 'y':
                            listPerpus[indexBuku][1] = ubahBuku
                        elif pilihan == 't':
                            mengubah()
                        else :
                            print('Masukkan pilihan yang benar'.center(90,'#'))
                    case 'Nama Peminjam':
                        ubahPeminjam = input('Mengubah nama peminjam: ').title()
                        pilihan = input('\nApakah anda ingin mengubah data? y/t: ').lower()
                        if pilihan == 'y':
                            listPerpus[indexBuku][2] = ubahPeminjam
                        elif pilihan == 't':
                            mengubah()
                        else :
                            print('Masukkan pilihan yang benar'.center(90,'#'))
                    case 'Alamat Peminjam':
                        ubahAlamat = input('Mengubah alamat peminjam: ').title()
                        pilihan = input('\nApakah anda ingin mengubah data? y/t: ').lower()
                        if pilihan == 'y':
                            listPerpus[indexBuku][3] = ubahAlamat
                        elif pilihan == 't':
                            mengubah()
                        else :
                            print('Masukkan pilihan yang benar'.center(90,'#'))
                    case 'Tanggal Peminjam':
                        ubahTanggal = input('Mengubah Tanggal: ')
                        pilihan = input('\nApakah anda ingin mengubah data? y/t: ').lower()
                        if pilihan == 'y':
                            listPerpus[indexBuku][4] = ubahTanggal
                        elif pilihan == 't':
                            mengubah()
                        else :
                            print('Masukkan pilihan yang benar'.center(90,'#'))
                    case _:
                        print('Kolom tidak ditemukan'.center(90,'#'))
            else :
                print('Data tidak ditemukan'.center(90,'#'))
                mengubah()


        elif pilihan == '2':
            break
        else:
            print('Masukkan pilihan yang benar'.center(90,'#'))

# Menghapus
def hapus():
    while True:
        print('Menu 4'.center(90,'='))
        print('1. Menghapus data peminjaman buku')
        print('2. Kembali ke menu')

        pilihan = input('Pilih menu: ')
        if pilihan == '1':
            data()
            print('Menu 4'.center(90,'='))
            buku = input('Masukkan kode buku yang ingin di hapus: ').title()
            cek = mengecek(buku)
            indexBuku = mengecekIndex(buku)
            if cek :
                pilihan = input('\nApakah anda ingin menghapus data? y/t: ').lower()
                if pilihan == 'y':
                    listPerpus.pop(indexBuku)
                    print(f'Data {buku} berhasil dihapus')
                elif pilihan == 't':
                    mengubah()
                else :
                    print('Masukkan pilihan yang benar'.center(90,'#'))
            else:
                print('Data tidak ditemukan'.center(90,'#'))
                hapus()
        elif pilihan == '2':
            break
        else:
            print('Masukkan pilihan yang benar'.center(90,'#'))
    

# Main menu
def main():
    while True:
        print('SELAMAT DATANG DI PROGRAM PEMINJAMAN BUKU'.center(90,'='))
        print('Menu 1 : Menampilkan data peminjaman buku')
        print('Menu 2 : Menambahkan data peminjaman buku')
        print('Menu 3 : Mengubah data peminjaman buku')
        print('Menu 4 : Menghapus data peminjaman buku')
        print('Menu 5 : Menyortir berdasarkan kolom')
        print('Menu 6 : Exit program')

        pilihan = input('Pilih menu: ')

        if pilihan == '1':
            tampil()
        elif pilihan == '2':
            tambah()
        elif pilihan == '3':
            mengubah()
        elif pilihan == '4':
            hapus()
        elif pilihan == '5':
            sort()
        elif pilihan == '6':
            print('Terimakasih telah menggunakan program ini')
            break
        else :
            print('Masukkan pilihan yang benar'.center(90,'#'))


# Menjalankan program
main()