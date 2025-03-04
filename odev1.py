# Boş öğrenci listesi
ogrenciler = []

while True:
    # Öğrenci ismi al
    isim = input("Öğrenci ismini gir (Çıkmak için 'q' bas): ")

    if isim.lower() == 'q':  # 'q' girilirse çık
        break


    notlar = input(f"{isim} için notları gir (Virgülle ayır): ")


    not_listesi = [int(n) for n in notlar.split(",")]


    ogrenciler.append({"isim": isim, "notlar": not_listesi})

print("\n Öğrenci Not Ortalamaları ")
for ogrenci in ogrenciler:
    ortalama = sum(ogrenci["notlar"]) / len(ogrenci["notlar"])  # Ortalama hesapla
    print(f"{ogrenci['isim']} adlı öğrencinin not ortalaması: {ortalama:.2f}")
