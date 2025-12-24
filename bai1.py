M = int(input())
a = [1, 2, 3, 6, 7, 8, 9]
b = sorted(a)
tong = 0
for i in range(1, len(a)):
    if i % M == 0:
        tong += b[i]
print(tong)

