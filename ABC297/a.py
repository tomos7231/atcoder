N, D = map(int, input().split())
T = list(map(int, input().split()))

for id in range(N - 1):
    if T[id + 1] - T[id] <= D:
        print(T[id + 1])
        exit()
print(-1)
