# coding: utf-8
#




cntNum = input() # 要素数の取得

numList = [int(num) for num in input().split()] #コマンドライン入力数値の取得


cntDivision = 0 # 割り算回数の初期化
isOdd = False # 奇数判定フラグの初期化



while True:

    # 入力数値を1つずつ２で除算して余りが0でなかったら、奇数判定フラグをTrueにする

    for num in numList:

        if (num % 2 != 0):

            isOdd = True

    # 奇数判定フラグがFalseなら（除算した結果奇数が含まれていなかったら）除算を実行
    # 奇数判定フラグがTrueなら、whileループを抜ける
    if (isOdd == False):

        numList = [ (num/2) for num in numList ]

        cntDivision += 1

    else:

        break



print(cntDivision)