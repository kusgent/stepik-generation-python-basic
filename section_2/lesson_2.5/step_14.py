# https://stepik.org/lesson/284816/step/14?auth=login&unit=266160

num = int(input())
a = num // 100
b = (num % 100) // 10
c = num % 10

print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
