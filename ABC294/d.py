# N, Qを入力
N, Q = map(int, input().split())
# 受付に行った人の集合
gone = set()
# イベント3の時のmin
min = 1
# イベントを入力
for i in range(Q):
    event = list(map(int, input().split()))
    # イベントが1の場合は受付に呼ばれる（呼ばれてない人の中で最小の人）
    if event[0] == 1:
        continue
    # イベントが2の場合は受付に行く
    elif event[0] == 2:
        gone.add(event[1])
    # イベントが3の場合は呼ばれている人の中で受付に行ってない人が再度呼ばれる
    elif event[0] == 3:
        # N人を順番に見ていく（最も小さい人を呼んでいるため）
        while True:
            if min not in gone:
                print(min)
                break
            else:
                min += 1
