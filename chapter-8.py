###############################################################
# 8. 선택 정렬  
###############################################################

# 8-0-1 선택 정렬 알고리즘
# a: 리스트

# def find_min_idx(a):
#     n = len(a)
#     min_idx = 0
#     for i in range(1, n):
#         if a[i] < a[min_idx]:
#             min_idx = i
#     return min_idx

# def sel_sort(a):
#     result = []
#     while a:
#         min_idx = find_min_idx(a)
#         value = a.pop(min_idx)
#         result.append(value)
#     return result

# d = [2, 4, 5, 1, 3]
# print(sel_sort(d))

# def sel_sort(a):
#     n = len(a)
#     for i in range(0, n - 1): # 0부터 n-2까지 반복
#         # i번 위치부터 끝까지 자료 값 중 최솟값의 위치를 찾음
#         min_idx = i
#         for j in range(i + 1, n):
#             if a[j] < a[min_idx]:
#                 min_idx = j
#         # 찾은 최솟값을 i번 위치로
#         a[i], a[min_idx] = a[min_idx], a[i]
        
# d = [2, 4, 5, 1, 3]
# sel_sort(d)
# print(d)

# 8-2
def reverse_sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
        
d = [2, 4, 5, 1, 3]
reverse_sel_sort(d)
print(d)