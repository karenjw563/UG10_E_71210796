#menginput daftar siswa 
A = ((input("Masukkan daftar siswa : ")))
print("Daftar siswa : ", A.title().split(","))

#menginput siswa yang ingin ditambahkan
B = ((input("Masukkan siswa yang ingin ditambahkan : ")))

#mendapatkan hasil
if B not in A :
    print ("Hasil penambahan pada daftar siswa : ", [A.title(), B.upper()])
else: 
    print("Siswa atas nama", (B.upper()), "sudah berada dalam daftar siswa.")