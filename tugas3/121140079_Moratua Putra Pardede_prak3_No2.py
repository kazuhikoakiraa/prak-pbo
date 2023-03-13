class AkunBank:
    list_pelanggan = {}
    def __init__(self, norekening, nama, saldo):
        self._norekening = norekening
        self._nama = nama
        self._saldo = saldo

        AkunBank.list_pelanggan.update({self._norekening : self._nama})
        self.menu = 0

    def opening(self):
        print("Halo ", self._nama, ", selamat datang di Bank Zeus")
        print()

    def lihat_saldo(self):
        print ("saldo Anda saat ini Rp ", self._saldo)

    def tarik_tunai(self):
        self.nominal_tarik = int(input("Masukkan jumlah nominal yang ingin Anda WD: "))
        if self.nominal_tarik > self._saldo:
            print("Saldo Anda tidak mencukupi, sadar udah rungkad bang.")
        else:
            print("WD berhasil!")
            self._saldo -= self.nominal_tarik

    def transfer(self):
        self.nominal_transfer = int(input("Masukkan jumlah nominal yang ingin Anda transfer: "))
        if self.nominal_tarik <= self._saldo:
            self.rekening_tujuan = int(input("Masukkan nomor rekening tujuan: "))
            if self.rekening_tujuan in AkunBank.list_pelanggan:
                print ("Transfer Rp ", self.nominal_transfer, " ke ", AkunBank.list_pelanggan[self.rekening_tujuan]," sukses! ")
                self._saldo -= self.nominal_transfer
            else :
                print("Nomor rekening tujuan tidak ditemukan!")
                print("Kembali ke menu utama...")
        else:
            print("Saldo Anda tidak mencukupi untuk melakukan transaksi, depo dulu kali.")

    def lihat_menu(self):
        
        print("Pilih menu transaksi yang ingin Anda lakukan :")
        print("1. Lihat Saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")
        print()
        self.menu=int(input("Masukkan pilihan: "))
        if self.menu == 1:
          AkunBank.lihat_saldo(self)
        elif self.menu == 2:
          AkunBank.tarik_tunai(self)
        elif self.menu == 3:
          AkunBank.transfer(self)

Akun1 = AkunBank(1234, "Moratua Putra", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

Akun1.opening()
while Akun1.menu < 4:
    Akun1.lihat_menu()
    print(" ")