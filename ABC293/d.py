class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        # 根ならその番号を返す
        if self.parents[x] < 0:
            return x
        # 根でないなら、親の番号を更新して返す
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)
        # 根が同じなら何もしない
        if x == y:
            return
        # 根が違うなら、xの根をyの根につなげる
        else:
            # xの根をyの根につなげる
            self.parents[x] = y

    def same(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    N, M = [int(nm) for nm in input().split()]
    # union findを作る
    uf = UnionFind(N)
    x = 0
    for _ in range(M):
        a, b, c, d = input().split()
        a, c = int(a) - 1, int(c) - 1
        if uf.same(a, c):
            x += 1
        # くっつける
        uf.union(a, c)

    y = 0
    for i in range(N):
        # 根の数を数える
        if uf.parents[i] < 0:
            y += 1

    print(x, y - x)
