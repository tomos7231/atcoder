N = int(input())
A = [int(a) for a in input().split()]
# 偶数を格納するリスト
even = []
for a in A:
    if a % 2 == 0:
        even.append(a)
# 空白区切りで出力
print(*even, sep=" ")
