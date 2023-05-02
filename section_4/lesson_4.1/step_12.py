# https://stepik.org/lesson/265081/step/12?auth=login&unit=246029

num1 = int(input())
num2 = int(input())
num3 = int(input())

res = 0

if num1 > 0:
    res = num1
if num2 > 0:
    res += num2
if num3 > 0:
    res += num3

print(res)
