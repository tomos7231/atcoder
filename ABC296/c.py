# N, Xを入力
N, X = map(int, input().split())
# Aを入力
A = list(map(int, input().split()))


def find_combination(A, X):
    # Aの集合バージョンを作成
    A_set = set(A)
    # Aの要素を回す
    for a in A:
        target = a + X
        # targetがAの集合に含まれている場合
        if target in A_set:
            return True
    # for文が終わったらFalseを返す
    return False


# Xが0の場合
if X == 0:
    print("Yes")
else:
    # find_combination関数を呼び出す
    if find_combination(A, X):
        print("Yes")
    else:
        print("No")
