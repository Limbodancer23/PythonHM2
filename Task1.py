# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
n = int(input("Enter number of coins: "))
CoinNum = 0
FirstSide = 0
while CoinNum < n:
    CoinSide = int(input("Enter 0 or 1: "))
    if CoinSide == 0:
        FirstSide+=1
    CoinNum+=1
if FirstSide >= n - FirstSide:
    print(f"The requied coin number needed to be turned over: {n - FirstSide}")
elif n - FirstSide >= FirstSide:
    print(f"The requied coin number needed to be turned over: {FirstSide}")