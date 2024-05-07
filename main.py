import db

def add():
    kode_barang = input("Masukan Kode Barang : ")
    nama_barang = input("Masukan Nama Barang : ")
    harga_barang = int(input("Masukan Harga Barang : "))
    stock_barang = int(input("Masukan stock Barang : "))

    db.create_item(kode_barang, nama_barang, harga_barang, stock_barang)

def read():
    print("""
+===========================+
   DATA BARANG DI GUDANG
+===========================+""")
    items = db.read_item()
    print()
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stock_barang = item[4]
        print(f"""
+---------------------------+
Kode  Barang  : {kode_barang}
Nama  Barang  : {nama_barang}
Harga Barang  : {harga_barang}
Stock Barang  : {stock_barang}
+---------------------------+""")

def delete():
  kode = input("Masukan kode barang yang akan dihapus : ")
  db.delete_item(kode)

def update():
    print("""
+===========================+
 EDIT DATA BARANG DI GUDANG
+===========================+""")
    kode = input("Masukan kode barang yang akan diedit : ")
    kode_barang = input("Masukan Kode Barang Baru : ")
    nama_barang = input("Masukan Nama Barang Baru : ")
    harga_barang = int(input("Masukan Harga Barang Baru : "))
    stock_barang = int(input("Masukan stock Barang Baru : "))
    db.updateData(kode_barang, nama_barang, harga_barang, stock_barang, kode)


def start():
    while True:
        print("""
+===========================+
    PROGRAM GUDANG CRUD
+===========================+
1. TAMBAH DATA KE GUDANG
2. CEK DATA GUDANG
3. HAPUS DATA DARI GUDANG
4. EDIT DATA GUDANG
5. KELUAR PROGRAM
+===========================+""")
        menu = input('Pilih Menu : ')

        if menu == "1":
            add()
        elif menu == "2":
            read()
        elif menu == "3":
            delete()
        elif menu == "4":
            update()
        elif menu == "5":
            exit()
        else :
          print("INVALID")

if __name__ == '__main__':
  start()