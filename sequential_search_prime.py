#Latihan 1

def sequential_search_prime (y) :
    if y <= 1 :
        return False
    for i in range (2, int (y**0.5) + 1) :
        if y % i == 0 :
            return False
    return True

def prime_numbers(angka) :
    AngkaPrima = []
    for a in angka :
        if sequential_search_prime(a) :
            AngkaPrima.append(a)
    return AngkaPrima

angka = [7, 10, 13, 6, 17, 22, 19]
AngkaPrima = prime_numbers (angka)
print ("Bilangan prima yang ada pada angka tersebut adalah : ", AngkaPrima)