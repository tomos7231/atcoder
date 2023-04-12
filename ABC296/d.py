# N, Mを入力
N, M = map(int, input().split())

# Nの2乗がMより小さい場合は-1
if N**2 < M:
    print(-1)
    exit()
else:
    # Nの範囲でfor文
    for i in range(1, N + 1):
        # iの2乗がM以上の場合
        if i**2 >= M:
            # i*i-1, i-1*i+1がMを超えているか判定
            if i * (i - 1) >= M:
                print(i * (i - 1))
                exit()
            elif (i - 1) * (i + 1) >= M:
                print((i - 1) * (i + 1))
                exit()
            else:
                print(i * i)
                exit()
        else:
            continue
print(-1)
