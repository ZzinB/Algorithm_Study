def check(perm, signs):
    # 부등호를 확인하여 조건 체크
    for i in range(len(signs)):
        if signs[i] == '<' and not (perm[i] < perm[i+1]):
            return False
        if signs[i] == '>' and not (perm[i] > perm[i+1]):
            return False
    return True

def find_numbers(k, signs):
    from itertools import permutations
    
    numbers = list(range(10))
    max_value = ""
    min_value = ""
    
    # 모든 순열에 대해 체크
    for perm in permutations(numbers, k+1):
        if check(perm, signs):
            num = ''.join(map(str, perm))
            if not max_value or num > max_value:
                max_value = num
            if not min_value or num < min_value:
                min_value = num
                
    return max_value, min_value

k = int(input())  # 부등호 개수
signs = input().split()  # 부등호 기호 입력

max_value, min_value = find_numbers(k, signs)

print(max_value)
print(min_value)