# https://stepik.org/lesson/265082/step/5?auth=login&unit=246030

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num2 >= num1 >= num3 or num2 <= num1 <= num3:
    print(num1)
elif num1 >= num2 >= num3 or num1 <= num2 <= num3:
    print(num2)
else:
    print(num3)
