H, W = [int(hw) for hw in input().split()]
for _ in range(H):
    S = []
    # Aを入力
    A = [int(a) for a in input().split()]
    for a in A:
        if a == 0:
            # 対応するところが0ならSはピリオド
            S.append(".")
        else:
            # そうじゃない時はアルファベット（大文字Aのコードポイントを足すことに注意）
            S.append(chr(a - 1 + ord("A")))
    print("".join(S))
