# https://stepik.org/lesson/284816/step/13?auth=login&unit=266160

num = int(input())
first_digit = num // 100
second_digit = (num % 100) // 10
third_digit = num % 10

print("Сумма цифр =", first_digit + second_digit + third_digit)
print("Произведение цифр =", first_digit * second_digit * third_digit)
