###############################################################
# 14. 동명이인 찾기
###############################################################

# 14-1 딕셔너리를 이용해 동명이인 찾기

def find_same_name(a):
    
    name_dict = {}
    for name in a: # 리스트 a에 있는 자료들을 차례로 반복
        if name in name_dict:     
            name_dict[name] += 1
        else: # 새 이름이면
            name_dict[name] = 1

    result = set()  # 결괏값을 저장할 빈 집합
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]

# print(find_same_name(name))
# print(find_same_name(name2))

# 연습문제 14-1 번호로 이름 찾기

def get_name(info_dic, find_num):
    if find_num in info_dic:
        return info_dic[find_num]
    else:
        return "?"

sample_info = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}

print(get_name(sample_info, 105))
print(get_name(sample_info, 777))