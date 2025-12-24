a = list(map(int, input().split()))
dem_max = 0
so = None
for x in a:
    dem = a.count(x)
    if dem > dem_max or (dem == dem_max and x > so):
        dem_max = dem
        so = x
print(so)
