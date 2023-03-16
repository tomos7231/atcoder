H, W = [int(hw) for hw in input().split()]
HW = []
for _ in range(H):
    A = [int(a) for a in input().split()]
    HW.append(A)

# 嬉しい経路数
ans = 0
# 経路全列挙
for order in range(2 ** (H + W - 2)):
    h, w = 0, 0
    # マスの管理
    seen = set()
    seen.add(HW[0][0])
    # 経路の管理
    for i in range(H + W - 2):
        print("order:", order, "i:", i, "h:", h, "w:", w, "value:", order >> i & 1)
        if order >> i & 1:
            h += 1
            # 外に出ちゃってる
            if h == H:
                break
            # 嬉しくない
            if HW[h][w] in seen:
                break

        else:
            w += 1
            # 外に出ちゃってる
            if w == W:
                break
            # 嬉しくない
            if HW[h][w] in seen:
                break
        seen.add(HW[h][w])
    else:
        print(seen)
        ans += 1
print(ans)
