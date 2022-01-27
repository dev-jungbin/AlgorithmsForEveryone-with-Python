###############################################################
# 13. 회문 찾기
###############################################################

# 13-1 회문 찾기
# 주어진 문장이 회문인지 아닌지 찾기(큐와 스택의 특징을 이용)
# 입력: 문자열 s
# 출력: 회문이면 True, 아니면 False
# lower() 소문자로 바꿈

def palindrome(s):
    
    qu = []
    st = []
    
    for x in s:
        
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
            
    while qu:  # 큐에 문자가 남아 있는 동안 반복
        if qu.pop(0) != st.pop():  # 큐와 스택에서 꺼낸 문자가 다르면 회문이 아님
            return False

    return True

# print(palindrome("Wow"))
# print(palindrome("Madam, I’m Adam."))
# print(palindrome("Madam, I am Adam."))

# 연습문제 13-1

def palindrome_practice(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].isalpha() == False:
            i += 1
        elif s[j].isalpha() == False:
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1

    return True

print(palindrome_practice("Wow"))
print(palindrome_practice("Madam, I’m Adam."))
print(palindrome_practice("Madam, I am Adam."))