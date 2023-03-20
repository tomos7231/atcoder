MOD = 998244353
N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]

# dpテーブル
# dp[i][flag] := i枚目までのカードの組み合わせのうち条件を満たしてi枚目のカードがflag（表か裏）であるようなものの個数
dp = [[0, 0] for _ in range(N)]
dp[0] = [1, 1]

for i in range(1, N):
    for pre in range(2):  # pre = 0 は1つ前のカードが表、pre = 1 は裏
        for nxt in range(2):  # nxt = 0 は現在のカードが表、nxt = 1 は裏
            if data[i - 1][pre] != data[i][nxt]:  # i-1枚目のカードとi枚目のカードの数字が異なる場合
                dp[i][nxt] += dp[i - 1][pre]  # i-1枚目の組み合わせ数を足す
    dp[i][0] = dp[i][0] % MOD
    dp[i][1] = dp[i][1] % MOD
print((dp[N - 1][0] + dp[N - 1][1]) % MOD)
