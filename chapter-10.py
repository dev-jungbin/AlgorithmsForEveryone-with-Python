###############################################################
# 10. 병합 정렬  
###############################################################

# 10-1병합 정렬 알고리즘(풀어서, return O)

# def merge_sort(a):
#     n = len(a)
#     # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음
#     if n <= 1:
#         return a
#     # 그룹을 나누어 각각 병합 정렬을 호출
#     mid = n // 2                # 중간을 기준으로 두 그룹으로 나눔(mid: 몫)
#     g1 = merge_sort(a[:mid])    # 재귀 호출로 첫 번째 그룹 정렬
#     g2 = merge_sort(a[mid:])    # 재귀 호출로 두 번째 그룹 정렬
    
#     result = []
#     while g1 and g2:            # 두 그룹 하나씩 반복(마지막 자료 남을 때까지)
#         if g1[0] < g2[0]:       # 두 그룹 [0] 값 비교
#             result.append(g1.pop(0))    #g1 값이 더 작으면 그 값을 pop하여 result에 append
#         else:
#             result.append(g2.pop(0))    #g2 값이 더 작으면~
    
#     while g1:
#         result.append(g1.pop(0))
#     while g2:
#         result.append(g2.pop(0))
        
#     return result

# d = [2, 45, 2, 3, 4, 51, 20, 35, 66, 47]
# print(merge_sort(d))

# 10-2 병합 정렬 알고리즘(return X)

# def merge_sort(a):
#     n = len(a)
    
#     if n <= 1:
#         return
    
#     mid = n // 2
#     g1 = a[:mid]
#     g2 = a[mid:]
    
#     merge_sort(g1)
#     merge_sort(g2)
    
#     i1 = 0
#     i2 = 0
#     ia = 0
    
#     while i1 < len(g1) and i2 < len(g2):
#         if g1[i1] < g2[i2]:
#             a[ia] = g1[i1]
#             i1 += 1
#             ia += 1
#         else:
#             a[ia] = g2[i2]
#             i2 += 1
#             ia += 1
            
#     # 아직 남아 있는 자료들을 결과에 추가
#     while i1 < len(g1):
#         a[ia] = g1[i1]
#         i1 += 1
#         ia += 1
#     while i2 < len(g2):
#         a[ia] = g2[i2]
#         i2 += 1
#         ia += 1
            
# d = [12, 234, 5, 12, 66, 3, 53, 83, 46, 38, 22, 1 ,10]
# merge_sort(d)
# print(d)    

# 연습문제 10-1, 내림차순 병합 정렬

def merge_sort(a):
    n = len(a)
    
    if n <= 1:
        return
    
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    
    merge_sort(g1)
    merge_sort(g2)
    
    i1 = 0
    i2 = 0
    ia = 0
    
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] > g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
            
    # 아직 남아 있는 자료들을 결과에 추가
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
            
d = [12, 234, 5, 12, 66, 3, 53, 83, 46, 38, 22, 1 ,10]
merge_sort(d)
print(d)    