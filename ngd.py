import math
def NormalizedGoogleDistance(x,y,z):
    lx = math.log2(x)
    ly = math.log2(y)
    lz = math.log2(z)

    N = 25270000000000
    
    ngd = (max(lx,ly)- lz)/(math.log2(N)- min(lx,ly))
    return ngd

x = 11970000000
y = 3830000000
z = 4320000000

l = NormalizedGoogleDistance(x,y,z)
print(l)