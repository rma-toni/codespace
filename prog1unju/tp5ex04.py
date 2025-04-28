#n = int(input("n: "))
#s = 0
#i = 3
#
#while(i < n):
#    s += i
#    i+=2
#print(s)

n = int(input('n: '))
i = 3
s = 0
f1 = 1
f2 = 1
while i <= n:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    if i % 2 != 0:
        s += f3
    i += 1
print(s)

#n  i   s   f1  f2  f3    i<=n    i%2!=0
#6  3   0   1   1   -     true    true
#6  4   2   1   2   2     true    false
#6  5   2   2   3   3     true    true   
#6  6   7   3   5   5     true    false
#6  7   7   5   8   8     false   true
#6
#6