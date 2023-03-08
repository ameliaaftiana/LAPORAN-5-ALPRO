print("Program Perhitungan IPS Mahasiswa")

matkul=int(input("Masukkan jumlah matkul = "))
list=[]
jumlah=0

for i in range(matkul):
    nilai=(input(f"Masukkan matkul {i+1} = "))
    list.append(nilai)

for i in range (matkul):
    if list[i] == "A":
        jumlah = jumlah + 4
    elif list[i] == "B":
        jumlah = jumlah + 3
    elif list[i] == "C":
        jumlah = jumlah + 2
    elif list[i] == "D":
        jumlah = jumlah + 1
ips=((jumlah*3)/matkul)/3

print("Nilai IPS anda semester ini", round(ips, 2))
