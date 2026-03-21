
#phan tich thua so nguyen to
def bs(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
n = int(input())
tmp = n
i, prod = tmp//2, 1
ls, arr = [], []
while n != 1:
    if n % i == 0:
        if prod - (tmp//prod) >= 0:
            ls.append([prod, tmp//prod])
            arr.append(prod - tmp//prod)
        n //= i
        prod *= i
    else:
        i += 1
print(ls[bs(arr, min(arr))])