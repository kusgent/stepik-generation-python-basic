# https://stepik.org/lesson/265083/step/11?auth=login&unit=246031

num = int(input())

if 0 < num // 1000 < 10 and (num % 7 == 0 or num % 17 == 0):
    print("YES")
else:
    print("NO")
