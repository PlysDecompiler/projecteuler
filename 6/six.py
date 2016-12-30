#https://projecteuler.net/problem=6

# 1+2+3+4+...+n = (n^2+n)/2 -> (1+2+3+4+...+n)^2 = (n^4+2n^3+n^2)/4
# 1^2+2^2+3^2+4^2+...+n^2 = n*(n+1)*(2n+1)/6
# solution: (n^4+2n^3+n^2)/4-n*(n+1)*(2n+1)/6 = n^4/4+n^3/6-n^2/4-n/6

n = 100
solution = n**4/4+n**3/6-n**2/4-n/6
print solution
#25164150
