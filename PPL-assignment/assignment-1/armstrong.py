s = int(input('Enter Starting no.\n'))
e = int(input('Enter Ending no.\n'))
f = 0
for i in range(s, e + 1):
    t = i
    r = 0
    while(t > 0):
        r += (t % 10)**3
        t //= 10
    if(r == i):
        print('Armstrong no. : ', r)
        f = 1
if(not f):
    print('no Armstrong no. in the given range')
