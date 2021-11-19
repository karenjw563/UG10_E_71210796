print("==== Kalkulator Akar dan Pangkat ====")
print("Pilihan menu :\n1. Pangkat 2 (Kuadrat)\n2. Pangkat 3 (Kubik)\n3. Akar Kuadrat")

Menu = int(input("Masukkan menu yang anda pilih: "))
if Menu == 1:
    Data = int(input("Masukan bilangan yang ingin dipangkatkan: "))
    Result = (Data ** 2)
    print("Hasil dari perpangkatan bilangan", Data, "dengan", "2 adalah", Result)
elif Menu == 2:
    Data = int(input("Masukkan bilangan yang ingin dipangkatkan: "))
    Result = (Data ** 3)
    print("Hasil dari perpangkatan bilangan", Data, "dengan", "3 adalah", Result)
elif Menu == 3:
    Data = int(input("Masukkan bilangan yang ingin dipangkatkan: "))
    Result = float(Data ** (1/2))
    print("Hasil dari akar pangkat dua dari bilangan", Data, "adalah", Result)
else: 
    print("Pilihan menu yang dimasukkan tidak sesuai")