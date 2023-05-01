# https://stepik.org/lesson/265081/step/6?auth=login&unit=246029

num = int(input())

first_digit = num // 1000
second_digit = (num // 100) % 10
third_digit = (num // 10) % 10
last_digit = num % 10

if first_digit + last_digit == second_digit - third_digit:
    print("ДА")
else:
    print("НЕТ")
