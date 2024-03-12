class Person:
    def __init__(self, nama, umur, alamat):
        self.__nama = nama       # Atribut privat
        self.__umur = umur       # Atribut privat
        self.__alamat = alamat   # Atribut privat

    # Metode untuk mengambil nilai atribut
    def get_nama(self):
        return self.__nama
    
    def get_umur(self):
        return self.__umur
    
    def get_alamat(self):
        return self.__alamat
    
    # Metode untuk mengubah nilai atribut
    def set_nama(self, nama_baru):
        self.__nama = nama_baru
    
    def set_umur(self, umur_baru):
        self.__umur = umur_baru
    
    def set_alamat(self, alamat_baru):
        self.__alamat = alamat_baru

# Contoh penggunaan
p = Person("goku", 30, "Jakarta")
print("Nama:", p.get_nama())      # Output: goku
print("Umur:", p.get_umur())      # Output: 30
print("Alamat:", p.get_alamat())  # Output: Jakarta

# Mengubah nilai atribut
p.set_nama("bejita")
p.set_umur(35)
p.set_alamat("Bandung")

print("\nSetelah diubah:")
print("Nama:", p.get_nama())      # Output: bejita
print("Umur:", p.get_umur())      # Output: 35
print("Alamat:", p.get_alamat())  # Output: Bandung
