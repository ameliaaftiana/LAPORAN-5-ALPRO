
angka=int(input("Masukkan angka yang mau dikalikan = "))
kali=int(input("Masukkan perkalian = "))

def perkalian(angka, kali):
    hasil=0
    print(f"{angka} X {kali} = ", end="")
    for i in range(1, angka+1):
        if i == angka:
            print(f"{kali} = ", end="")
        else:
            print(f"{kali} + ", end="") 
        hasil = hasil + kali 
    print (f" {hasil}")

perkalian(angka,kali)