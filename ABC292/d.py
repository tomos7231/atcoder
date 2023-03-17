from collections import deque

N, M = [int(nm) for nm in input().split()]
# 自己ループしている辺の数を管理
table = [0 for _ in range(N)]
G = [[] for _ in range(N)]
# 辺の数だけ入力を受け取る
for _ in range(M):
    u, v = [int(a) - 1 for a in input().split()]
    # ループ辺はtableに記録
    if u == v:
        table[u] += 1
    else:
        # それぞれの接続頂点情報に記録
        G[u].append(v)
        G[v].append(u)

seen = [False for _ in range(N)]
for i in range(N):
    if seen[i]:
        continue

    que = deque()
    que.append(i)
    # この連結成分に含まれる頂点と辺の数
    e, v = 0, 0
    # この連結成分に含まれる自己ループ辺の数
    eself = 0
    while que:
        # 先頭削除
        now = que.popleft()
        # 頂点と自己ループ辺の数を更新
        v += 1
        eself += table[now]
        seen[now] = True
        for nex in G[now]:
            e += 1
            if not seen[nex]:
                seen[nex] = True
                que.append(nex)

    # 条件に合わない場合はNO
    if v != e // 2 + eself:
        print("No")
        exit()

print("Yes")
