H, W = map(int, input().split())
# resultを初期化
result = []
# 再起的に入力
for _ in range(H):
    S = list(input())
    # 長さWについて、2個ずつ見ていく
    for i in range(W - 1):
        # 2個ともTなら、最初をP、次をCで置き換える
        if S[i] == "T" and S[i + 1] == "T":
            S[i] = "P"
            S[i + 1] = "C"
    # resultに追加
    result.append("".join(S))

for _ in range(H):
    # result出力
    print(result[_])
