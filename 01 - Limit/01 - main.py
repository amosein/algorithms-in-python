from typing import List
"""

[1, 2, 3, 4, 5]
we have min and max for a list and if we have
min(3) it gives us this : [3, 4, 5]
and
max(3) it gives us this : [1, 2, 3]
and if both at the same time
min, max = 3 -> [3]

"""

# Best Practice
def limit(data, min=None, max=None):
    min_check = lambda val: True if min is None else (val >= min)
    max_check = lambda val: True if max is None else (val <= max)

    return [val for val in data if min_check(val) and max_check(val)]

print(limit([1, 2, 3, 4, 5], max=3))

# # My way - 1
# data = [1, 2, 3, 4, 5]
#
# min_ = int(input("Enter min : "))
# max_ = int(input("Enter max : "))
# if min_ != 0 and max_ != 0:
#     pass
#
# elif min_ != 0:
#     pass
# elif max_ != 0:
#     pass

# # My way 2
# def limit(data: List, max_ :int = 0, min_ :int = 0):
#     result = []
#
#     if max_ == 0:
#         for i in data:
#             if i <= min_:
#                 result.append(i)
#     elif min_ == 0:
#         for j in data:
#             if j >= max_:
#                 result.append(j)
#
#     elif max_ == min_:
#         return [max_]
#
#     return result
#
# data = [1, 2, 3, 4, 5]
# # max_ = int(input("Max = "))
# # min_ = int(input("Min = "))
# print(limit(data, 3, 0))
