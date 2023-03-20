# memo:https://qiita.com/kitadakyou/items/6f877edd263f097e78f4
N = int(input())
S = input()
# 原点
x, y = 0, 0
# setで既出位置を管理
visit = set()
# 既出位置に原点を追加
visit.add((0, 0))

for s in S:
    # 4方向に移動
    if s == "L":
        x -= 1
    elif s == "R":
        x += 1
    elif s == "U":
        y += 1
    elif s == "D":
        y -= 1

    # 既出位置に現在位置があればYes
    if (x, y) in visit:
        print("Yes")
        exit()

    # 既出位置に追加
    visit.add((x, y))

# 既出位置に現在位置がなければNo
print("No")
