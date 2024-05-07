import mysql.connector
import time

db = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='curdpy'
)

def create_item(kode_barang, nama_barang, harga_barang, stock_barang):
    cursor = db.cursor()
    cursor.execute(
      "INSERT INTO gudangpy (kode_barang, nama_barang, harga_barang, stock_barang) VALUES (%s, %s, %s, %s)",
      (kode_barang, nama_barang, harga_barang, stock_barang)
      )
    db.commit()

    if cursor.rowcount > 0:
        print(
            """ 
+===========================+
  DATA BERHASIL DITAMBAHKAN
+===========================+""")
        time.sleep(1)
    else:
        print(
            """ 
+===========================+
   DATA GAGAL DITAMBAHKAN
+===========================+""")
        time.sleep(1)

def read_item():
  cursor = db.cursor()
  cursor.execute("SELECT * FROM gudangpy")
  return cursor.fetchall()

def delete_item(kode):
    cursor = db.cursor()
    query = "DELETE FROM gudangpy WHERE kode_barang = %s"
    cursor.execute(query, (kode,))
    db.commit()
    if cursor.rowcount > 0:
        print(
            """ 
+===========================+
   DATA BERHASIL DIHAPUS
+===========================+""")
        time.sleep(1)
    else:
        print(
            """ 
+===========================+
   DATA GAGAL DIHAPUS
+===========================+""")
        time.sleep(1)

def updateData(kode_barang, nama_barang, harga_barang, stock_barang, kode):
    cursor = db.cursor()
    cursor.execute(
        "UPDATE gudangpy SET kode_barang = %s, nama_barang = %s, harga_barang = %s, stock_barang = %s WHERE kode_barang = %s",
        (kode_barang, nama_barang, harga_barang, stock_barang, kode),
    )
    db.commit()
    if cursor.rowcount > 0:
        print(
            """ 
+===========================+
   DATA BERHASIL DIEDIT
+===========================+"""
        )
        time.sleep(1)
    else:
        print(
            """ 
+===========================+
   DATA GAGAL DIEDIT
+===========================+"""
        )
        time.sleep(1)