# 自然数Nを入力
N = int(input())
X = [int(a) for a in input().split()]
# Xを昇順にソート
X.sort()
# 有効なのはリストの前後N個を除いたもの
X = X[N:-N]
print(sum(X) / len(X))
