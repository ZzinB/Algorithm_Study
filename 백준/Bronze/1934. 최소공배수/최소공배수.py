t = int(input())

def gcd(a, b): #최대공약수(유클리드 호제법)
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for i in range(t):
    a, b = map(int, input().split())
    result = a * b / gcd(a, b) #최대공약수를 이용해 최소공배수
    print(int(result))