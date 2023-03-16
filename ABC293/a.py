# https://atcoder.jp/contests/abc293/tasks/abc293_a
# 文字列を1文字ごとに格納
S = list(input())
for i in range(1, len(S) // 2 + 1):
    S[2 * i - 2], S[2 * i - 1] = S[2 * i - 1], S[2 * i - 2]
print("".join(S))
