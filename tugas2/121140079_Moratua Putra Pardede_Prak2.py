class Mora:
    def __init__(self,nama,nim,kelas,sks):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks = sks
    def Cetak(self):
        print("Berikut adalah data mahasiswa :")
        print("Nama :",self.nama)
        print("NIM :",self.nim)
        print("Kelas PBO Siakad :",self.kelas)
        print("Jumlah SKS :",self.sks)
mahasiswa = Mora("Moratua Puta Pardede",121140079,"RB",22)
mahasiswa.Cetak()