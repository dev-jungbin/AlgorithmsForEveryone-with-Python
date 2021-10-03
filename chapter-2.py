###############################################################
# 2. 최댓값 찾기
###############################################################

# 2-0
def c2_0(numList):
    max = numList[0]
    for i in range(0, len(numList)):
        if max < numList[i]:
            max = numList[i]
    return max

# 2-0-1
def c2_0_1(numList):
    maxIdx = 0
    temp = numList[0]
    for i in range(0, len(numList)):
        if temp < numList[i]:
            temp = numList[i]
            maxIdx = i
    return maxIdx
 
# 2-1
def c2_1(numList):
    min = numList[0]
    for i in range(0, len(numList)):
        if min > numList[i]:
            min = numList[i]
    return min

print(c2_0([1, 23, 29, 12, 39, 7, 15]))
print(c2_0_1([1, 23, 29, 12, 39, 7, 15]))
print(c2_1([1, 23, 29, 12, 39, 7, 15]))