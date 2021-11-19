Suhu = float(input("Masukkan suhu tubuh Anda : "))
if Suhu > 50:
    print("Anda bukan Manusia :)")
elif Suhu < 32:
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
elif 50 >= Suhu >= 37.5:
    print("Anda demam! Jangan bepergian ke tempat fasilitas Umum. ")
else:
    print("Suhu Anda normal!")