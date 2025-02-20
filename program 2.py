class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def tampil(self):
        return f"{self.judul} by {self.penulis}"

Buku1 = Buku("Pulang", "Tere Liye")
Buku2 = Buku("Filosofi Teras", "Henry Manampiring")
Buku3 = Buku("The Midnight Library", "Matt Haig")

print(Buku1.tampil())
print(Buku2.tampil())
print(Buku3.tampil())

