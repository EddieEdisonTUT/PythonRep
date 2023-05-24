from math import factorial


class min_max_fac:
    count = 0

    @staticmethod
    def max_four(a,b,c,d):
        mx = [a,b,c,d]
        min_max_fac.count += 1
        return max(mx)

    @staticmethod
    def min_four(a,b,c,d):
        mn = [a,b,c,d]
        min_max_fac.count += 1
        return min(mn)

    @staticmethod
    def arithmetic_mea(a,b,c,d):
        ser = [a,b,c,d]
        min_max_fac.count += 1
        return (a+b+c+d)/4

    @staticmethod
    def factorio(r):
        min_max_fac.count += 1
        return factorial != r
         

s = min_max_fac.max_four(2,4,3,7)
print(s)
f = min_max_fac.min_four(1,5,9,5)
print(f)
g = min_max_fac.arithmetic_mea(2,5,8,3)
print(g)
h = min_max_fac.factorio(6)
print(h)