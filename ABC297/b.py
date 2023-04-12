S = list(input())
b_list = []
r_list = []
k_list = []
for i in range(8):
    if S[i] == "K":
        k_list.append(i + 1)
    if S[i] == "B":
        b_list.append(i + 1)
    if S[i] == "R":
        r_list.append(i + 1)

if (
    (b_list[0] % 2 != b_list[1] % 2)
    and (r_list[0] < k_list[0])
    and (r_list[1] > k_list[0])
):
    print("Yes")
else:
    print("No")
