###############################################################
# 9. 삽입 정렬  
###############################################################

# 9-0-1 삽입 정렬 알고리즘
# a: 리스트

# def find_ins_idx(r, v):
#     for i in range(0, len(r)):
#         if v < r[i]:
#             return i
#     return len(r)

# def ins_sort(a):
#     result = []
#     while a:
#         value = a.pop(0)
#         ins_idx = find_ins_idx(result, value)
#         result.insert(ins_idx, value)
#     return result

# d = [2, 4, 5, 1, 3]
# print(ins_sort(d))

# 9-0-2 삽입 정렬 알고리즘
# a: 리스트

# def ins_sort(a):
#     n = len(a)
#     for i in range(1, n):
#         key = a[i]
#         j = i - 1
#         while j >= 0 and a[j] > key:
#             a[j + 1] = a[j]
#             j -= 1
#         a[j + 1] = key

# d = [2, 4, 5, 1, 3]
# ins_sort(d)
# print(d)

# 9-2 삽입 정렬 알고리즘 - 내림차순
# a: 리스트

def reverse_ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        
d = [2, 4, 5, 1, 3, 1, 2, 1, 5, 6, 7, 2, 3, 0]
reverse_ins_sort(d)
print(d)