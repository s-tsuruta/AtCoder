# coding: utf-8

numN, otoshidamaY = map(int, input().split())

listMoney = []

for i in range(numN+1):
    for j in range(numN+1-i):
        sumMoney = 10000*i + 5000*j +1000*(numN-i-j)
        if (otoshidamaY == sumMoney):
            listMoney = [i, j ,numN-i-j]
            break
if (listMoney):
    print(" ".join([str(num) for num in listMoney]))
else:
    print("-1 -1 -1")