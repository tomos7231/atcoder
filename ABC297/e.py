import heapq

# N, Kを入力
N, K = map(int, input().split())
# Aを入力
A = list(map(int, input().split()))


def find_kth_min_price(prices, k):
    heap = []
    visited = set()
    for price in prices:
        # ヒープに値を追加
        heapq.heappush(heap, price)
        visited.add(price)

    count = 0
    # k-1回繰り返す
    while count < k - 1:
        print("ヒープの中身: ", heap)
        # ヒープから最小値を取り出す
        min_price = heapq.heappop(heap)
        # 他の値との計算を行う
        for price in prices:
            new_price = min_price + price
            # まだ訪れていない値のみヒープに追加
            if new_price not in visited:
                heapq.heappush(heap, new_price)
                visited.add(new_price)
                count += 1

    return heapq.heappop(heap), visited


kth_min_price, visited = find_kth_min_price(A, K)
print(kth_min_price)
print(visited)
