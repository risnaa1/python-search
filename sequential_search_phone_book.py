#Latihan 2

def sequential_search (BukuTelp, nama) :
    for kontak in BukuTelp :
        if kontak[0] == nama :
            return kontak[1]
    return "Nomor telepon anda tidak ditemukan."

BukuTelp = [
    ["John Doe", "081234567890"],
    ["Jane Smith", "098876543210"],
    ["Michael Johnson", "08711223344"],
    ["Emily Davis", "082122232425"]
]

name = "Jane Smith"
NomorTelp = sequential_search (BukuTelp, name)

if NomorTelp != "Nomor telepon tidak ditemukan.":
    print (f"Nomor telepon {name} adalah {NomorTelp}.")
else :
    print(NomorTelp)