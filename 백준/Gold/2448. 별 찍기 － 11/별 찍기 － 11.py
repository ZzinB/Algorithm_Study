n = int(input())

def star(m):
    if m == 3:
        return ['  *  ',' * * ','*****']
    arr = star(m//2)
    stars = []
    for i in arr:
        stars.append(' ' * (m//2) + i + ' ' * (m//2))
    for i in arr:
        stars.append(i + ' ' + i)
    return stars

print('\n'.join(star(n)))