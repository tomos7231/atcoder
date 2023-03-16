# https://atcoder.jp/contests/abc293/tasks/abc293_b
K = int(input())
X = list(map(int, input().split()))
call_list = [0 for _ in range(K)]
for i in range(K):
    # もしcall_listのi番目が0ならば、X[i]に対応するcall_listの要素を1にする
    if call_list[i] == 0:
        call_list[X[i] - 1] = 1
    else:
        continue
# call_listが0の数を数える
print(call_list.count(0))
# call_listが0の要素のインデックスを出力する
for i in range(K):
    if call_list[i] == 0:
        print(i + 1, end=" ")
