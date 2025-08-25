# # For цикъл - повтаря някакво действие точно определен брой пъти
# for number in range(1, 11):  # range = диапазон
#     print(number)


# While цикъл - повтаря някакво действие докато дадено условие е вярно
is_hungry = False
bites = 0  # bites = хапки

while is_hungry:
    bites = bites + 1
    print("+1 хапка")

    if bites == 4:
        print("Вече се нахраних!")
        is_hungry = False
