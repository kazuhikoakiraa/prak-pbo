class Robot:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.jumlah_turn = 0

    def lakukan_aksi(self, lawan):
        print(self.name, " menyerang ", lawan.name, " sebanyak ", self.damage, " DMG")
        lawan.health -= self.damage
        if self.jumlah_turn % 3 == 2 and isinstance(self, Antares):
            self.damage = int(self.damage * 1.5)
            print(self.name, " meningkatkan damage menjadi ", self.damage, " DMG")
        elif self.jumlah_turn % 2 == 1 and isinstance(self, Alphasetia):
            self.health += 4000
            print(self.name, " menambah darah sebanyak 4000 HP")
        elif self.jumlah_turn % 4 == 3 and isinstance(self, Lecalicus):
            self.health += 7000
            self.damage = int(self.damage * 2)
            print(self.name, " meningkatkan damage menjadi ", self.damage, " DMG dan menambah darah sebanyak 7000 HP")
        self.jumlah_turn += 1

    def terima_aksi(self, lawan):
        print(self.name, " menerima serangan dari ", lawan.name, " sebanyak ", lawan.damage, " DMG")
        self.health -= lawan.damage

class Antares(Robot):
    def __init__(self):
        super().__init__("Antares", 50000, 5000)

class Alphasetia(Robot):
    def __init__(self):
        super().__init__("Alphasetia", 40000, 6000)

class Lecalicus(Robot):
    def __init__(self):
        super().__init__("Lecalicus", 45000, 5500)

print("Selamat datang di pertandingan robot Yamako")
print("Pilih robot :")
print("1 = Antares, 2 = Alphasetia, 3 = Lecalicus")
print("masukan pilihan : ")
robot = int(input())
if robot == 1:
    robotmu = Antares()
elif robot == 2:
    robotmu = Alphasetia()
elif robot == 3:
    robotmu = Lecalicus()
else:
    print("Pilihan robotmu tidak tersedia")
    exit()

print("Pilih robot lawan :")
print("1 = Antares, 2 = Alphasetia, 3 = Lecalicus")
print("masukan pilihan : ")
robot_lawan = int(input())
if robot_lawan == 1:
    lawan = Antares()
elif robot_lawan == 2:
    lawan = Alphasetia()
elif robot_lawan == 3:
    lawan = Lecalicus()
else:
    print("Pilihan lawan tidak tersedia")
    exit()

print("1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")
for turn in range(1, 6):
    print("Turn saat ini : ", turn)
    print("Robotmu ", robotmu.name, " ",  robotmu.health, " HP,  robot lawan ", lawan.name, " ", lawan.health, " HP")
    robot = int(input("Pilih tangan robotmu : "))
    robot_lawan = int(input("Pilih tangan robot lawan : "))
    if robot == 1 and robot_lawan == 2:
        lawan.lakukan_aksi(robotmu)
    elif robot == 1 and robot_lawan == 3:
        robotmu.lakukan_aksi(lawan)
    elif robot == 2 and robot_lawan == 1:
        lawan.lakukan_aksi(robotmu)
    elif robot == 2 and robot_lawan == 3:
        robotmu.lakukan_aksi(lawan)
    elif robot == 3 and robot_lawan == 1:
        lawan.lakukan_aksi(robotmu)
    elif robot == 3 and robot_lawan == 2:
        robotmu.lakukan_aksi(lawan)
