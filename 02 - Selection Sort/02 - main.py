# Selection Sort

import random
# My way 2 - Success :)
list1 = [random.randint(0, 10) for i in range(10)]

for i in range(len(list1) - 1):
    small = i

    for j in range(i, len(list1)):
        if list1[j] < list1[small]:
            small = j

    list1[i], list1[small] = list1[small], list1[i]
print(list1)

# My way 1 - Failed
# unsorted = [4, 3, 0, 1, 9]

# lenght = len(unsorted)
# # menhaye 1 chon nmikhaym ta enteha bere
# # 0 1 2 3
# for i in range(lenght - 1):
#     print(f"i = {i}")
#     original = unsorted[i]
#     small = unsorted[i]
#     index_outer = i
#     for j in range(i, lenght):
#         print(f"j = {j}")
#         if unsorted[j] < small:
#             small = unsorted[j]
#             index_inner = j
#             print(small)
#     print(f"unsorted[i] = small")
#     unsorted[index_inner], unsorted[index_outer] = small, original
#     print(f"small = {small}")
#     print(unsorted)
#
# print(unsorted)

