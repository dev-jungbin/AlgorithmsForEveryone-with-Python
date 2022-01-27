###############################################################
# 15. 친구의 친구 찾기
###############################################################

# 15-1 딕셔너리를 이용해 동명이인 찾기
def print_all_friends(g, start):
    qu = [] # 앞으로 처리해야 할 사람들을 큐에 저장
    done = set() # 이미 큐에 추가한 사람들을 집합에 기록(중복 방지)

    qu.append(start) # 자신을 큐에 넣고 시작
    done.add(start) # 집합에 추가

    while qu: # 큐에 처리할 사람이 남아 있는 동안
        p = qu.pop(0) # 큐에서 처리 대상
        print(p)
        for x in g[p]: # 그의 친구들 중에
            if x not in done: # 아직 큐에 추가된 적이 없는 사람을
                qu.append(x) # 큐에 추가
                done.add(x) # 집합에 추가

fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

# print_all_friends(fr_info, 'Summer')
# print()
# print_all_friends(fr_info, 'Jerry')

def print_all_friendship(g, start):
    qu = [] # 기억 장소 1: 앞으로 처리해야 할 (사람 이름, 친밀도) 튜플을 큐에 저장
    done = set() # 기억 장소 2: 이미 큐에 추가한 사람을 집합에 기록(중복 방지)

    qu.append((start, 0)) # (사람 이름, 친밀도) 정보를 하나의 튜플로 처리
    done.add(start) # 집합에 추가

    while qu: # 큐에 처리할 사람이 남아 있는 동안
        (p, d) = qu.pop(0) # 큐에서 (사람 이름, 친밀도) 정보를 p와 d로 각각 꺼냄
        print(p, d) # 사람 이름과 친밀도를 출력
        for x in g[p]: # 친구들 중에
            if x not in done: # 아직 큐에 추가된 적이 없는 사람
                qu.append((x, d + 1)) # 친밀도를 1 증가시켜 큐에 추가
                done.add(x)
                
print_all_friendship(fr_info, 'Summer')
print()
print_all_friendship(fr_info, 'Jerry')