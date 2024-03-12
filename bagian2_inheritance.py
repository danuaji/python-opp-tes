class Vehicle:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna
    
    def berkendara(self):
        print(f"Mobil {self.warna} {self.merek} sedang dikendarai.")

class Car(Vehicle):
    def __init__(self, merek, warna, jumlah_pintu):
        super().__init__(merek, warna)
        self.jumlah_pintu = jumlah_pintu
    
    def klakson(self):
        print("Telolet telolet!")

class Bicycle(Vehicle):
    def __init__(self, merek, warna, jumlah_gigi):
        super().__init__(merek, warna)
        self.jumlah_gigi = jumlah_gigi
    
    def bunyikan_bell(self):
        print("Kring kring!")

# Contoh penggunaan
mobil = Car("Toyota", "merah", 4)
mobil.berkendara()   # Output: Mobil merah Toyota sedang dikendarai.
mobil.klakson()      # Output: Telolet telolet!

sepeda = Bicycle("Polygon", "biru", 6)
sepeda.berkendara()       # Output: Mobil biru Giant sedang dikendarai.
sepeda.bunyikan_bell()   # Output: Kring kring!
