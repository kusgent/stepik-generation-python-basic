# https://stepik.org/lesson/284816/step/15?auth=login&unit=266160

num = int(input())
first_digit = num // 1000
second_digit = (num % 1000) // 100
third_digit = (num % 100) // 10
fourth_digit = num % 10

print("Цифра в позиции тысяч равна", first_digit)
print("Цифра в позиции сотен равна", second_digit)
print("Цифра в позиции десятков равна", third_digit)
print("Цифра в позиции единиц равна", fourth_digit)
