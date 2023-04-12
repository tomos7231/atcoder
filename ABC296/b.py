# 行と列を定義
retu = ["a", "b", "c", "d", "e", "f", "g", "h"]
gyou = ["8", "7", "6", "5", "4", "3", "2", "1"]

# 文字列が8回入力される
for i in range(8):
    # 文字列をinput
    S = list(input())
    # for文で文字列を回す
    for j in range(8):
        # 文字列がアスタリスクの場合
        if S[j] == "*":
            # 行と列を結合して出力
            print(retu[j] + gyou[i])
