###############################################################
# 3. 동명이인 찾기(1)
###############################################################

# 3-0
def c3_0(array):
    answer = set()
    
    for i in range(0, len(array)):
        first_name = array[i]
        for j in range(i + 1, len(array)):
            if first_name == array[j]:
                answer.add(first_name)
    return answer

name_array = ["Tom", "Jerry", "Merry", "Mike", "Jerry", "Tom", "Ann", "Tom"]
print("동명이인 찾기", c3_0(name_array))

# 3-1
def c3_1(array):
    answer = []

    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            answer.append(array[i] + " - " + array[j])
    for x in answer:
        print(x)


simple_name_array = ["Tom", "Jane", "Ann"]
c3_1(simple_name_array)

# 3-2
## A. O(1)
## B. O(n)
## C. O(n^2)
## D. O(n^4)