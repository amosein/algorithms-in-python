# Selection Sort

# My way
unsorted = [4, 3, 0, 1, 9]

lenght = len(unsorted)
# menhaye 1 chon nmikhaym ta enteha bere
# 0 1 2 3
for i in range(lenght - 1):
    print(f"i = {i}")
    original = unsorted[i]
    small = unsorted[i]
    index_outer = i
    for j in range(i, lenght):
        print(f"j = {j}")
        if unsorted[j] < small:
            small = unsorted[j]
            index_inner = j
            print(small)
    print(f"unsorted[i] = small")
    unsorted[index_inner], unsorted[index_outer] = small, original
    print(f"small = {small}")
    print(unsorted)

print(unsorted)