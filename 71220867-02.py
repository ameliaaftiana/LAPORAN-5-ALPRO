atas=int(input("Masukkan batas atas = "))
bawah=int(input("Masukkan batas bawah = "))

if bawah > atas:
    for i in range (bawah, atas-1, -1):
        if i % 2 == 1:
            if i == atas or i == atas + 1:
                print(i, end=" ")
            else:
                print (i, end=", ")
else:
    for i in range (bawah, atas+1,1):
        if i % 2 == 1:
            if i == atas or i == atas - 1:
                print(i, end=" ")
            else:
                print (i, end=", ")

