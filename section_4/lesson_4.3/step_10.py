# https://stepik.org/lesson/265082/step/10?auth=login&unit=246030

num = int(input())

if num < 0 or num > 36:
    print("ошибка ввода")
elif num == 0:
    print("зеленый")
elif 1 <= num <= 10 or 19 <= num <= 28:
    if num % 2 == 1:
        print("красный")
    else:
        print("черный")
elif 11 <= num <= 18 or 29 <= num <= 36:
    if num % 2 == 1:
        print("черный")
    else:
        print("красный")
