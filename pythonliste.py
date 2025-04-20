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
