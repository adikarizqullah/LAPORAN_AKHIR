a1,a2 = input().split()
a1 = int(a1)
a2 = int(a2)
hasil1 = 0
hasil2 = 0
hasil3 = 0
i = 0 
while i < a1:
    i += 1
    j = i
    if i==0:
        break
    while j > 0:
        j -= 1
        print("(%d * %d)" % (j + 1, a2), end=" ")
        if  j > 0:
            print(" + ", end=" ")
    hasil1 = i * a2
    hasil2 += hasil1
    print(" = %d" % (hasil2))
    hasil3 += hasil2
print("%d" % (hasil3))