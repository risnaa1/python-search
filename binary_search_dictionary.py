#Latihan 4

def search_definition(word, dictionary):
    x = 0
    y = len(dictionary) - 1

    while x <= y:
        mid = (x + y) // 2

        if dictionary[mid][0] == word:
            return dictionary[mid][1]
        elif dictionary[mid][0] < word:
            x = mid + 1
        else:
            y = mid - 1
    return "Definisi tidak ditemukan."

dictionary = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

word = "Banana"

definition = search_definition(word, dictionary)

print("Definisi dari kata", word, "adalah:", definition)
