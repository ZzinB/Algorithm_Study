import sys
input = sys.stdin.readline

n = int(input())
dna = list(input().rstrip())
itp = {"AG":"C", "AC":"A", "AT":"G", "GC":"T", "GT":"A", "CT":"G"}

a,b = "", dna.pop()
for _ in range(n-1):
    a = dna.pop()
    if a == b:
        continue
        
    if a+b in itp:
        b = itp[a+b]
    else:
        b = itp[b+a]
print(b)