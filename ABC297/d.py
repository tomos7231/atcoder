# A, Bを入力
A, B = map(int, input().split())
count = 0
shou = 0

# AとBが同じ場合は0
if A == B:
    print(0)
    exit()

# while
while True:
    # AまたはBが0の場合
    if A == 0 or B == 0:
        # AとBの和を出力
        print(count - 1)
        # 終了
        break
    else:
        # AがBより大きい場合
        if A > B:
            # 商もカウント
            shou = A // B
            # AをBで割った余りをAに代入
            A %= B

        # BがAより大きい場合
        elif B > A:
            # 商もカウント
            shou = B // A
            # BをAで割った余りをBに代入
            B %= A
        count += shou
