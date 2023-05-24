# https://stepik.org/lesson/265082/step/8?auth=login&unit=246030

num1 = int(input())
num2 = int(input())
string = input()

if string == '+':
    print(num1 + num2)
elif string == "-":
    print(num1 - num2)
elif string == "*":
    print(num1 * num2)
elif string == "/":
    if num2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(num1 / num2)
else:
    print("Неверная операция")
