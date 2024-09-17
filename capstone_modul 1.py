daftarbuku = [
    {
        'Kode' : 'GR2019',
        'Judul' : 'Gadis Kretek',
        'Penulis' : 'Ratih Kumala',
        'Kategori' : 'Novel',
        'Penerbit' : 'Gramedia Pustaka Utama',
    },
    {
        'Kode' : 'MR2017',
        'Judul' : 'Marmut Merah Jambu',
        'Penulis' : 'Raditya Dika',
        'Kategori' : 'Komedi',
        'Penerbit' : 'Bukune',
    },
    {
        'Kode' : 'TA2024',
        'Judul' : 'The Little Prince',
        'Penulis' : 'Antoine de Saint-Exupéry',
        'Kategori' : 'Fantasi',
        'Penerbit' : 'Norris Book',
    },
    {
        'Kode' : 'AJ2023',
        'Judul' : 'Atomic Habits',
        'Penulis' : 'James Clear',
        'Kategori' : 'Pengembangan Diri',
        'Penerbit' : 'Gramedia Pustaka Utama',
    },
    {
        'Kode' : 'BO2021',
        'Judul' : 'Bicara Itu Ada Seninya',
        'Penulis' : 'Oh Su Hyang',
        'Kategori' : 'Pengembangan Diri',
        'Penerbit' : 'Bhuana Ilmu Komputer',
    }
]

def daftar_buku():
    print('\n================== Daftar Buku ===================\n')
    print('-'*50)
    for i in range(len(daftarbuku)):
        print(f'index           :  {i+1}')
        print(f'kode            :  {daftarbuku[i]['Kode']}')
        print(f'Judul           :  {daftarbuku[i]['Judul']}')
        print(f'Penulis         :  {daftarbuku[i]['Penulis']}')
        print(f'Kategori        :  {daftarbuku[i]['Kategori']}')
        print(f'Penerbit        :  {daftarbuku[i]['Penerbit']}')
        print('-'*50)

def daftar_buku_list():
    print('\n=============== Daftar Buku ===============\n')
    print('Index | Kode     |  Judul')
    print('-------------------------------------------')
    for i in range(len(daftarbuku)):
        print(f'  {i+1}.  | {daftarbuku[i]['Kode']}   |  {daftarbuku[i]['Judul']}')
        print('-------------------------------------------')

def check(sample, item):
    for elem in sample:
        if item in elem.values():
            return True
    return False

def read_buku():
    while True:
        print('\n1. Menampilkan semua buku')
        print('2. Menampilkan buku secara spesifik')
        print('3. Kembali ke menu utama')
        print('--------------------------------------------------------')
        sub_menu = input('Masukkan nomor yang anda pilih: ')
        print('--------------------------------------------------------')
        if sub_menu == '1':
            if len(daftarbuku) != 0:
                daftar_buku()
            else:
                print('Tidak ada data ditemukan!')
        elif sub_menu == '2':
            if len(daftarbuku) != 0:
                daftar_buku_list()
                kode = input('\nMasukkan Kode buku: ')
                if check(daftarbuku,kode) == True:
                    for index in range(len(daftarbuku)):
                        for key in daftarbuku[index]:
                            if daftarbuku[index][key] == kode:
                                    print('------------------------------------------')
                                    print(f'kode            :  {daftarbuku[index]['Kode']}')
                                    print(f'Judul           :  {daftarbuku[index]['Judul']}')
                                    print(f'Penulis         :  {daftarbuku[index]['Penulis']}')
                                    print(f'Kategori        :  {daftarbuku[index]['Kategori']}')
                                    print(f'Penerbit        :  {daftarbuku[index]['Penerbit']}')
                                    print('------------------------------------------')
                else:
                    print('Data tidak ditemukan!')
            else:
                print('Tidak ada data ditemukan!')
        elif sub_menu == '3':
            break
        else:
            print('Masukkan angka yang benar!')

def create_buku():
    while True:
        print('\n1. Menambahkan Buku')
        print('2. Kembali ke Menu Utama')
        print('--------------------------------------------------------')
        sub_menu = input('Masukkan nomor yang anda pilih: ')
        print('--------------------------------------------------------')
        if sub_menu == '1':
            kode_buku = input('Masukkan Kode Buku: ')
            print('------------------')
            if check(daftarbuku,kode_buku) == True:
                print('Kode buku yang anda masukkan sudah ada!')
            else:
                judul_buku = input('Masukkan Judul Buku: ')
                print('------------------')
                penulis_buku = input('Masukkan Penulis Buku: ')
                print('------------------')
                kategori_buku = input('Masukkan Kategori Buku: ')
                print('------------------')
                penerbit_buku = input('Masukkan Penerbit Buku: ')
                print('------------------')
                while True: 
                    print(f'kode            :  {kode_buku}')
                    print(f'Judul           :  {judul_buku}')
                    print(f'Penulis         :  {penulis_buku}')
                    print(f'Kategori        :  {kategori_buku}')
                    print(f'Penerbit        :  {penerbit_buku}')
                    print('-'*50)
                    konfirmasi = input('Apakan anda yakin untuk menyimpan? (y/n) ').lower()
                    print('--------------------------------------------------------')
                    if konfirmasi == 'y':
                        daftarbuku.append({
                        'Kode' : kode_buku,
                        'Judul' : judul_buku,
                        'Penulis' : penulis_buku,
                        'Kategori' : kategori_buku,
                        'Penerbit' : penerbit_buku,})
                        print('===== Data Tersimpan =====')
                        print('--------------------------------------------------------')
                        break
                    elif konfirmasi == 'n':
                        print('===== Dibatalkan =====')
                        print('--------------------------------------------------------')
                        break
                    else:
                        print('Masukkan pilihan yang benar! (y/n)')
        elif sub_menu == '2':
            break
        else:
            print('Masukkan angka yang benar!')

def update_buku():
    while True:
        print('\n1. Mengupdate buku')
        print('2. Kembali ke Menu Utama')
        print('--------------------------------------------------------')
        sub_menu = input('Masukkan nomor yang anda pilih: ')
        if sub_menu == '1':
            if len(daftarbuku) != 0:
                daftar_buku_list()
                while True:
                    try:
                        idx = int(input('Masukkan index buku yang ingin di ubah: '))
                        # print('--------------------------------------------------------')
                        if idx > 0 and idx <= len(daftarbuku):
                            print(f'index           :  {idx}')
                            print(f'kode            :  {daftarbuku[idx-1]['Kode']}')
                            print(f'Judul           :  {daftarbuku[idx-1]['Judul']}')
                            print(f'Penulis         :  {daftarbuku[idx-1]['Penulis']}')
                            print(f'Kategori        :  {daftarbuku[idx-1]['Kategori']}')
                            print(f'Penerbit        :  {daftarbuku[idx-1]['Penerbit']}')
                            print('--------------------------------------------------------')
                            while True:
                                konfirmasi = input('Apakah anda yakin untuk mengubah data tersebut? (y/n) ').lower()
                                print('--------------------------------------------------------')
                                if konfirmasi == 'y':
                                    print('1. kode')
                                    print('2. Judul')
                                    print('3. Penulis')
                                    print('4. Kategori')
                                    print('5. Penerbit')
                                    print('--------------------------------------------------------')
                                    while True:
                                        ubah_data = input('Masukkan nomor keterangan yang ingin di ubah: ')
                                        print('--------------------------------------------------------')
                                        if ubah_data == '1':
                                            u_kode = input('Masukkan kode baru: ')
                                            daftarbuku[idx-1]['Kode'] = u_kode
                                            print('===== Data berhasil di ubah! =====')
                                            break
                                        elif ubah_data =='2':
                                            u_judul = input('Masukkan judul baru: ')
                                            daftarbuku[idx-1]['Judul'] = u_judul
                                            print('===== Data berhasil di ubah! =====')
                                            break
                                        elif ubah_data == '3':
                                            u_penulis = input('Masukkan penulis baru: ')
                                            daftarbuku[idx-1]['Penulis'] = u_penulis
                                            print('===== Data berhasil di ubah! =====')
                                            break
                                        elif ubah_data == '4':
                                            u_kategori = input('Masukkan kategori baru: ')
                                            daftarbuku[idx-1]['Kategori'] = u_kategori
                                            print('===== Data berhasil di ubah! =====')
                                            break
                                        elif ubah_data == '5':
                                            u_penerbit = input('Masukkan penerbit baru: ')
                                            daftarbuku[idx-1]['Penerbit'] = u_penerbit
                                            print('===== Data berhasil di ubah! =====')
                                            break
                                        else:
                                            print('Masukkan pilihan yang benar!(1-5)')
                                            print('--------------------------------------------------------')
                                    break
                                elif konfirmasi == 'n':
                                    print('===== Dibatalkan =====')
                                    break
                                else:
                                    print('Masukkan pilihan yang benar! (y/n)')
                                    print('--------------------------------------------------------')
                            break
                        else:
                            print('Masukan index yang benar!')
                            print('--------------------------------------------------------')
                    except ValueError:
                        print('Masukkan index yang benar!')
                        print('--------------------------------------------------------')
            else:
                print('Tidak ada data!')        
        elif sub_menu == '2':
            break
        else:
            print('Masukkan angka yang benar!')
            print('--------------------------------------------------------')

def delete_buku():
    while True:
        print('\n1. Menghapus Buku')
        print('2. Kembali ke Menu Utama')
        print('--------------------------------------------------------')
        sub_menu = input('Masukkan nomor yang anda pilih: ')
        if sub_menu == '1':
            if len(daftarbuku) != 0:
                daftar_buku_list()
                while True:
                    try:
                        delete_data = int(input('Masukkan Index buku yang ingin anda hapus: '))
                        if delete_data > 0 and delete_data <= len(daftarbuku):
                            print('--------------------------------------------------------')
                            print(f'Index           :  {delete_data}')
                            print(f'kode            :  {daftarbuku[delete_data-1]['Kode']}')
                            print(f'Judul           :  {daftarbuku[delete_data-1]['Judul']}')
                            print(f'Penulis         :  {daftarbuku[delete_data-1]['Penulis']}')
                            print(f'Kategori        :  {daftarbuku[delete_data-1]['Kategori']}')
                            print(f'Penerbit        :  {daftarbuku[delete_data-1]['Penerbit']}')
                            print('--------------------------------------------------------')
                            while True:
                                konfirmasi = input('Apakah anda yakin ingin menghapus data ini? (y/n) ').lower()
                                print('--------------------------------------------------------')
                                if konfirmasi == 'y':
                                    del daftarbuku[(delete_data-1)]
                                    print('===== Data terhapus! =====')
                                    break
                                elif konfirmasi == 'n':
                                    print('===== Dibatalkan =====')
                                    break
                                else :
                                    print('Masukkan pilihan yang benar!')
                            break
                        else:
                            print('Masukkan Index yang benar')
                    except ValueError:
                        print('Masukkan index yang benar!')
            else:
                print('Tidak ada data!')
                break
        elif sub_menu == '2':
            break
        else:
            print('\nMasukkan angka yang benar')

def main():
    while True:
        print('''
======== PERPUSTAKAAN ========             
Menu list :
1. Menampilkan daftar buku
2. Menambah buku
3. Update buku
4. Menghapus buku
5. keluar dari program 
===============================
          ''')
        menu = input('Masukkan angka yang dari menu yang ingin di jalankan: ')
        print('--------------------------------------------------------')
        if menu == '1':
            read_buku()
        elif menu == '2':
            create_buku()
        elif menu == '3':
            update_buku()
        elif menu == '4':
            delete_buku()
        elif menu == '5':
            print('Sampai Jumpa!')
            break
        else:
            print('Masukkan angka yang benar!')

main()
