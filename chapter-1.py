## 1-0
def c1(n):
    return (n * (n+1)) // 2 # 여기에서 // 이 기호는 정수 나눗셈!

## 1-1
def c1_1(n):
    answer = 0
    for i in range(1, n+1):
        answer += pow(i, 2)
    return answer

print(sum_1ton(10))
print(pow_sum(10))

## 1-2 O(n) -> n=1이면 제곱 한 번 더하기 한 번, n=2이면 제곱 두 번 더하기 두 번 ...

## 1-3 O(1) -> n과 무관하게 삼차식 한 번