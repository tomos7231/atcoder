# N, Sをinput
N = int(input())
S = list(input())

# 初期はS[0]
now = S[0]

# for文でSを回す
for i in range(1, N):
    # nowとS[i]が異なる場合
    if now != S[i]:
        # nowをS[i]に更新
        now = S[i]
    # nowとS[i]が同じ場合
    else:
        # Noを出力
        print("No")
        # break
        exit()
# for文が終わったらYesを出力
print("Yes")
