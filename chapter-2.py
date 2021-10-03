def find_max(numList):
    max = numList[0]
    for i in range(0, len(numList)):
        if max < numList[i]:
            max = numList[i]
    return max
 
print(find_max([1, 23, 29, 12, 39, 7, 15]))