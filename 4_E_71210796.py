Numeral1 = int(input("Masukkan bilangan 1 : "))
Numeral2 = int(input("Masukkan bilangan 2 : "))
Numeral3 = int(input("Masukkan bilangan 3 : "))

if Numeral1 < Numeral2 < Numeral3 : 
    print("Urutkan bilangan dari yang terkecil adalah", Numeral1, Numeral2, Numeral3)
elif Numeral1 < Numeral3 < Numeral2 :
    print("Urutkan bilangan dari yang terkecil adalah", Numeral1, Numeral3, Numeral2)
elif Numeral2 < Numeral3 < Numeral1 :
    print("Urutkan bilangan dari yang terkecil adalah", Numeral2, Numeral3, Numeral1)
elif Numeral2 < Numeral1 < Numeral3 :
    print("Urutkan bilangan dari yang terkecil adalah", Numeral2, Numeral1, Numeral3)
elif Numeral3 < Numeral1 < Numeral2 : 
    print("Urutkan bilangan dari yang terkecil adalah", Numeral3, Numeral1, Numeral2)
elif Numeral3 < Numeral2 < Numeral1 :
    print("Urutkan bilangan dari yang terkecil adalah", Numeral3, Numeral2, Numeral1)
elif Numeral1 == Numeral2 == Numeral3 : 
    print("Urutan bilangan dari yang terkecil adalah", Numeral1, Numeral2, Numeral3)
elif Numeral1 == Numeral2 > Numeral3 : 
    print("Urutan bilangan dari yang terkecil adalah", Numeral3, Numeral1, Numeral2)
elif Numeral1 == Numeral2 < Numeral3 :
    print("Urutan bilangan dari yang terkecil adalah", Numeral1, Numeral2, Numeral3)
elif Numeral1 == Numeral3 > Numeral2 :
    print("Urutan bilangan dari yang terkecil adalah", Numeral2, Numeral1, Numeral3)
elif Numeral1 == Numeral3 < Numeral2 :
    print("Urutan bilangan dari yang terkecil adalah", Numeral1, Numeral3, Numeral2)
elif Numeral2 == Numeral3 > Numeral1 : 
    print("Urutan bilangan dari yang terkecil adalah", Numeral1, Numeral2, Numeral3)
elif Numeral2 == Numeral3 < Numeral1 : 
    print("Urutan bilangan dari yang terkecil adalah", Numeral2, Numeral3, Numeral1)
elif Numeral2 == Numeral1 > Numeral3 :
    print("Urutan bilangan dari yang terkecil adalah", Numeral3, Numeral2, Numeral1)
elif Numeral2 == Numeral1 < Numeral3 :
    print("Urutan bilangan dari yang terkecil adalah", Numeral2, Numeral1, Numeral3)
elif Numeral3 == Numeral1 > Numeral2 :
    print("Urutan bilangan dari yang terkecil adalah", Numeral2, Numeral3, Numeral1)
elif Numeral3 == Numeral1 < Numeral2 :
    print("Urutan bilangan dari yang terkwcil adalah", Numeral3, Numeral1, Numeral2)
elif Numeral3 == Numeral2 > Numeral1 :
    print("Urutan bilangan dari yang terkecil adalah", Numeral1, Numeral3, Numeral2)
elif Numeral3 == Numeral2 < Numeral1 :
    print("Urutan bilangan dari yang terkecil adalah", Numeral3, Numeral2, Numeral1)
else:
    print("Urutan bilangan dari yang terkecil adalah", Numeral1, Numeral2, Numeral3)