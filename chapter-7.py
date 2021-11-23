###############################################################
# 7. 순차 탐색
###############################################################

# 7-0-1 순차 탐색 알고리즘
# a: 리스트
# x: 찾는 값

def c7_0_1(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i
    
    return -1

# array = [17, 92, 18, 33, 58, 7, 33, 42]
# print(c7_0_1(array, 92))

# 시간 복잡도
# 배열의 인덱스 개수가 n이라면 최대 n번 비교해야 하므로 시간 복잡도는 O(n)

def c7_1(a, x):
    n = len(a)
    answer = []
    for i in range(0, n):
        if x == a[i]:
            answer.append(i)
    return answer

# array = [17, 92, 18, 17, 33, 58, 7, 33, 42]
# print(c7_1(array, 17))

# 시간 복잡도
# 배열의 인덱스 개수가 n이라면 무조건 n번 비교해야 하므로 시간 복잡도는 O(n)

def c7_3(num_array, name_array, fine_num):
    n = len(num_array)
    for i in range(0, n):
        if fine_num == num_array[i]:
            return name_array[i]
    return "?"

# stu_no = [39, 14, 67, 105]
# stu_name = ["Justin", "John", "Mike", "Summer"] 
# print(c7_3(stu_no, stu_name, 12))  