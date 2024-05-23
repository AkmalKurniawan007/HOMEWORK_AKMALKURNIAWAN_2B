import stock as s
barang_list = []
while True:
        print("\nSelamat datang di program Manajemen Stok Barang!")
        print("Pilihan:")
        print("1. Tambah Data Barang")
        print("2. Edit Data")
        print("3. Hapus Data Barang")
        print("4. Cari Data")
        print("5. Tampilkan Data Barang")
        print("6. Tampilkan Jumlah Data")
        print("7. Keluar")
        
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == '1':
            nama = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah barang: "))
            barang_list.append({'nama': nama, 'jumlah': jumlah})
        elif pilihan == '2':
            item = int(input("Masukkan indeks data yang ingin diubah: ")) - 1
            nama_baru = input("Masukkan nama baru: ")
            jumlah_baru = int(input("Masukkan jumlah baru: "))
            s.edit_data(barang_list, item, nama_baru, jumlah_baru)
        elif pilihan == '3':
            item = int(input("Masukkan indeks data yang ingin dihapus: ")) - 1
            if 0 <= item < len(barang_list):
                del barang_list[item]
                print("Data berhasil dihapus")
            else:
                print("Indeks tidak valid")
        elif pilihan == '4':
            nama_barang = input("Masukkan nama barang yang ingin dicari: ")
            s.cari_data(barang_list, nama_barang)
        elif pilihan == '5':
            s.tampilkan_data(barang_list)
        elif pilihan == '6':
            s.hitung_jumlah_data(barang_list)
        elif pilihan == '7':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
