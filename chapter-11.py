###############################################################
# 11. 퀵 정렬  
###############################################################

# 11-1 퀵 정렬 알고리즘(풀어서, return O)

# def quick_sort(a):
#     n = len(a)
#     if n <= 1:
#         return a

#     pivot = a[-1] # 기준 정하기, 랜덤
#     less = []
#     greater = []
    
#     for i in range(0, n - 1): # 현재 마지막 값은 기준이므로
#         if a[i] < pivot: # 기준과 비교
#             less.append(a[i])
#         else:
#             greater.append(a[i]) # 크면 g2에
            
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# d = [12, 234, 5, 12, 66, 3, 53, 83, 46, 38, 22, 1 ,10]
# print(quick_sort(d)) 

# 11-2 퀵 정렬 알고리즘(return X)

def quick_sort_sub(a, start, end): # 범위를 지정하여 저렬
    if end - start <= 0: # 종료 조건
        return
    
    pivot = a[end]
    i = start
    
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    
    quick_sort_sub(a, start, i - 1)
    quick_sort_sub(a, i + 1, end)

def quick_sort(a):
    quick_sort_sub(a, 0, len(a) - 1)

d = [12, 234, 5, 12, 66, 3, 53, 83, 46, 38, 22, 1 ,10]
quick_sort(d)
print(d) 