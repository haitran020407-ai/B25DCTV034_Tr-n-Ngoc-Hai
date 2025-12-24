a = list(map(int, input().split()))
b = sorted(a)
tong_min = sum(b[:4])
tong_max = sum(b[-4:])
chech_lech = tong_max - tong_min
print(tong_min)
print(chech_lech)