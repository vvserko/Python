l = [1, 2,]
a = l
print(f'l[0]={l[0]} - {hex(id(l[0]))}')
print(f'a[0]={a[0]} - {hex(id(a[0]))}')
l[0] = 0
print(f'l[0]={l[0]} - {hex(id(l[0]))}')
print(f'a[0]={a[0]} - {hex(id(a[0]))}')
print()
n = 10
g = n

print(f'n={n} - {hex(id(n))}')
print(f'g={g} - {hex(id(g))}')
print()

n = 55

print(f'n={n} - {hex(id(n))}')
print(f'g={g} - {hex(id(g))}')