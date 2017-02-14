#https://projecteuler.net/problem=52

digits = '123456789'
x1 = 10
x2 = 100/6.
found = False
while not found:
    i = x1
    while i < x2:
        s = str(i)
        if '0' in s:
            i+=1
            continue
        d = {k: s.count(k) for k in digits}
        for n in range(2,7):
            news = str(n*i)
            if any(news.count(k) != d[k] for k in digits):
                break
        else:
            print i
            found = True
            break
        i+=1
    x1*=10
    x2*=10
    
#solution: 142857 (which is actually the recurring part of 1/7.)
