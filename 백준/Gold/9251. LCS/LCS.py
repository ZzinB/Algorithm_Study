a = input().strip()
b = input().strip()
 
li = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
 
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            li[i+1][j+1]=li[i][j] + 1
        else:
             li[i+1][j+1]=  max(li[i+1][j], li[i][j+1])
 
print(li[-1][-1])