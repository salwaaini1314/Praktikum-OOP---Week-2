class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi*self.sisi
    
    def keliling(self):
        return 4*self.sisi

Persegi1 = Persegi(5)
Persegi2 = Persegi(8)
Persegi3 = Persegi(10)

print(f"Persegi yang memiliki panjang sisi {Persegi1.sisi} cm, luasnya senilai {Persegi1.luas()} cm2 dan kelilingnya senilai {Persegi1.keliling()} cm")
print(f"Persegi yang memiliki panjang sisi {Persegi2.sisi} cm, luasnya senilai {Persegi2.luas()} cm2 dan kelilingnya senilai {Persegi2.keliling()} cm")
print(f"Persegi yang memiliki panjang sisi {Persegi3.sisi} cm, luasnya senilai {Persegi3.luas()} cm2 dan kelilingnya senilai {Persegi3.keliling()} cm")
