N = int(input())
W = input().split()
# Wをsetに変換
W = set(W)
# target_word
target = set(["and", "not", "that", "the", "you"])
# Wとtargetの共通集合が空集合であればNo
if len(W & target) == 0:
    print("No")
else:
    print("Yes")
