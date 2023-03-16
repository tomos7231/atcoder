# https://atcoder.jp/contests/abc292/tasks/abc292_c
def count_divisor(N):
    count = 0
    for i in range(1, N + 1):
        if i * i > N:
            break
        if N % i != 0:
            continue
        count += 1
        # 反対側を見てカウント
        if N // i != i:
            count += 1
    return count


if __name__ == "__main__":
    N = int(input())
    # 約数の個数を管理
    table = [0 for _ in range(N)]
    for i in range(1, N):
        table[i] = count_divisor(i)

    ans = 0
    # ABの組み合わせを全探索
    for i in range(1, N):
        ab = i
        cd = N - i
        ans += table[ab] * table[cd]
    print(ans)
