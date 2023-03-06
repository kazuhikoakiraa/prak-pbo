## ini soal nomor 1
n = int(input("Masukan nilai N : "))
for i in range (n):
    for j in range (n):
        print("*", end="")
    print()

##  ini soal nomor 2
for i in range(3):
    username = str(input("Username anda : "))
    password = int(input("Password anda : "))

    if username == "informatika" and password == 12345678:
        print("Berhasil login!")
        break
    elif i == 2:
        print("Akun anda terblokir!")
    else:
        print("Username atau password anda salah Coba lagi")