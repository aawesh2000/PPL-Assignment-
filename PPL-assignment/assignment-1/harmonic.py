print("enter how many harmonic numbers are required")
end = int(input())
m = 0
i = 0
p = []
while(m != end):
    i = i + 1
    k = []
    n = 0
    for j in range(1, i//2 + 1):
        if(i%j == 0):
            k.append(j)
            n = n + 1
    add = 0
    k.append(i)
    n = n + 1
    for l in k :
        add = add + (i/l)
    add = add/i
    r = n/add
    if(r%1 == 0):
        p.append(i)
        m = m + 1
print(p)