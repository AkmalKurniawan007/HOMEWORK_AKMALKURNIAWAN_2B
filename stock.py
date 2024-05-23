def tampilkan_data(barang_list):
    if not barang_list:
        print("Data Barang Kosong")
    else:
        for index, barang in enumerate(barang_list):
            print(f"{index + 1}. Nama: {barang['nama']}, Jumlah: {barang['jumlah']}")


def hitung_jumlah_data(barang_list):
    print(f"Jumlah data yang tersimpan: {len(barang_list)}")


def cari_data(barang_list, nama_barang):
    hasil = [barang for barang in barang_list if barang['nama'].lower() == nama_barang.lower()]
    if hasil:
        for barang in hasil:
            print(f"Nama: {barang['nama']}, Jumlah: {barang['jumlah']}")
    else:
        print("Data tidak ditemukan")


def edit_data(barang_list, indeks, nama_baru, jumlah_baru):
    if 0 <= indeks < len(barang_list):
        barang_list[indeks]['nama'] = nama_baru
        barang_list[indeks]['jumlah'] = jumlah_baru
        print("Data berhasil diubah")
    else:
        print("Indeks tidak valid")
