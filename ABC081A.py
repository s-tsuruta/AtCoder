# inputでコマンド入力の数字を取得し、listに渡して一文字ずつ配列に格納
# inputで取得された数字はすべて文字列型で格納されているので、intで数値に変換
binDigit = [int(num) for num in list(input())]



# 配列の合計を計算。各配列要素の１の個数＝各配列の合計値

sumNum = sum(binDigit)



print(sumNum)



#問題設定は入力文字が3桁で限定されているから、上記のようにfor文を使う必要はない。