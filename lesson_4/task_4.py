name = input("Как се казваш?: ")
colour = input("Кой е любимият ти цвят?: ")
food = input("Коя е любимата ти храна?: ")
animal = input("Кое е любимото ти животно?: ")
number = int(input("Кажи едно число от 1 до 10: "))

tails = "опашки"
if number == 1:
    tails = "опашка"

print(f"Ти си {colour} {food}{animal} с {number} {tails}. Супергерой с име {name}.💥")
