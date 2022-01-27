###############################################################
# 12. 이분 탐색 
###############################################################

# 12-1 이분 탐색(마치 like... upDown 게임)
# 리스트에서 특정 숫자 위치 찾기(중간)
# 입력: 리스트 a, 찾는 값 x
# 출력: 찾으면 그 값의 위치, 찾지 못하면 -1

def binary_search(a, x):
    # 탐색할 범위를 저장하는 변수 start, end
    # 리스트 전체를 범위로 탐색 시작(0 ~ len(a)-1)
    
    start = 0
    end = len(a) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
            
    return -1

d = [1, 3, 6, 12, 22, 53, 62, 77, 82, 90]

# print(binary_search(d, 90))
# print(binary_search(d, 2))

# 연습 문제 12-1 재귀 호출을 사용한 이분 탐색
def binary_search_recursion_sub(a, x, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search_recursion_sub(a, x, mid + 1, end)
    else:
        return binary_search_recursion_sub(a, x, start, mid - 1)
    
    return -1

def binary_search_recursion(a, x):
    return binary_search_recursion_sub(a, x, 0, len(a) - 1)

print(binary_search_recursion(d, 90))
print(binary_search_recursion(d, 2))

