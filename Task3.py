# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
N = int(input("Enter N: "))
num = 1
count = 0
while count <= N:
    print(f"2^{count} = {num}")
    num*=2
    count+=1
