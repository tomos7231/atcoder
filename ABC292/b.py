# https://atcoder.jp/contests/abc292/tasks/abc292_b
N, Q = map(int, input().split())
xy = [map(int, input().split()) for _ in range(Q)]
x, y = [list(i) for i in zip(*xy)]

sensyu = [0 for i in range(N)]

for event in range(Q):
    if x[event] == 1:
        sensyu[y[event] - 1] += 1
    elif x[event] == 2:
        sensyu[y[event] - 1] += 2
    elif x[event] == 3:
        if sensyu[y[event] - 1] >= 2:
            print("Yes")
        else:
            print("No")
