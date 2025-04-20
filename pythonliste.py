liste = []

def eleman_ekle(eleman):
    liste.append(eleman)
    print(f"{eleman} listeye eklendi.")

def listeyi_goster():
    if not liste:
        print("Liste boş.")
    else:
        print("Listedeki elemanlar:")
        for index, item in enumerate(liste):
            print(f"{index + 1}. {item}")
def eleman_sil(index):
    if 1 <= index <= len(liste):
        silinen_eleman = liste.pop(index - 1)
        print(f"{silinen_eleman} listeden silindi.")
    else:
        print("Geçersiz indeks.")

while True:
    print("\n--- Liste Düzenleyici ---")
    print("1. Eleman Ekle")
    print("2. Listeyi Göster")
    print("3. Eleman Sil")
    print("4. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin (1-4): ")

    if secim == '1':
        eleman = input("Eklemek istediğiniz elemanı girin: ")
        eleman_ekle(eleman)
    elif secim == '2':
        listeyi_goster()
    elif secim == '3':
        if liste:
            try:
                index = int(input("Silmek istediğiniz elemanın numarasını girin: "))
                eleman_sil(index)
            except ValueError:
                print("Geçersiz giriş. Lütfen bir sayı girin.")
        else:
            print("Liste boş, silinecek eleman yok.")
    elif secim == '4':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen 1 ile 4 arasında bir sayı girin.")