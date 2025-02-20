class Warna:
    def __init__(self, warna, kode_warna):
        self.warna = warna
        self.kode_warna = kode_warna
    def show_warna(self):
        return f"\nWarna: {self.warna} \nKode warna = {self.kode_warna}"
        
Warna1 = Warna("Wisteria", "#8E44AD")
Warna2 = Warna("Silver", "#BDC3C7")

print(Warna1.show_warna())
print(Warna2.show_warna())
