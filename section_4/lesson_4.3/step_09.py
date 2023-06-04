# https://stepik.org/lesson/265082/step/9?auth=login&unit=246030

first_color = input()
second_color = input()

if first_color != "красный" and first_color != "синий" and first_color != "желтый" or second_color != "красный" and second_color != "синий" and second_color != "желтый":
    print("ошибка цвета")
elif first_color == second_color:
    print(first_color)
elif first_color == "красный":
    if second_color == "синий":
        print("фиолетовый")
    elif second_color == "желтый":
        print("оранжевый")
elif first_color == "синий":
    if second_color == "красный":
        print("фиолетовый")
    elif second_color == "желтый":
        print("зеленый")
elif first_color == "желтый":
    if second_color == "синий":
        print("зеленый")
    elif second_color == "красный":
        print("оранжевый")
