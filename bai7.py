import math

def cac_cap_so(ds, N):
    uoc_chung_max = 0
    for i in range(N):
        a, b = ds[i][0], ds[i][1]
        uoc_chung = math.gcd(a, b)
        
        # Cập nhật giá trị lớn nhất
        if current_gcd > max_val:
            uoc_chung_max = uoc_chung
            
    return uoc_chung_max

