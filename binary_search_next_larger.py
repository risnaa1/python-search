#Percobaan 9

def binary_search_next_larger(data, target) :
    low = 0
    high = len(data) - 1
    next_larger = None

    while low <= high :
        mid = (low + high) // 2
        if data[mid] > target :
            next_larger = data[mid]
            high = mid - 1
        else :
            low = mid + 1
        
    return next_larger

my_list = [2, 4, 6, 8, 10, 14]
target = 7 
result = binary_search_next_larger(my_list, target)
if result :
    print(f"Elemen terkecil yang lebih besar dari {target} adalah {result}")
else : 
    print("Tidak ada elemen yang lebih besar dari target.")

#Jadi elemen yang lebih besar dari 7 adalah 8. jika elemen 7 indeksnya 3 maka elemen 8 indeksnya 4
