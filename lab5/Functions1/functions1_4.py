def is_prime(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt = cnt + 1
    if cnt == 2:
        return True
    
    return False

nums = input().split()
filtered = [x for x in nums if is_prime(int(x))]
print(filtered)