class Manusia:
    def __init__(self, Nama, Umur):
        self.Nama = Nama
        self.Umur = Umur

    def tampilkan_data(self):
        return f"\nNama : {self.Nama} \nUmur : {self.Umur}"

name = input("Masukkan nama: ")
age = input("Masukkan umur: ")

hasil = Manusia(name, age)

print(hasil.tampilkan_data())

