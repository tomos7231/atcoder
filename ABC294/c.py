# N, Mを入力
N, M = map(int, input().split())
# Aを入力
A = set(map(int, input().split()))
# Bを入力
B = set(map(int, input().split()))
# AとBのsetの和集合
C = list(sorted(A | B))
# 連結した数列で、A, Bそれぞれのidxを格納する
A_idx = []
B_idx = []
for idx in range(N + M):
    # C[idx]がAにあるか
    if C[idx] in A:
        A_idx.append(idx + 1)
    else:
        B_idx.append(idx + 1)
print(" ".join(map(str, A_idx)))
print(" ".join(map(str, B_idx)))
