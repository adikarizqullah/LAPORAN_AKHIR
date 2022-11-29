def reverse (reserved):
    p = 0
    while reserved!= 0:
        p = (10*p) + reserved %10
        reserved //=10
    
    return p

for p in range(3):
    n1, n2 = input().split()
    n1 = reverse(int(n1))
    n2 = reverse(int(n2))
    hasil = n1 + n2
    print(f'\n{reverse(hasil)}')