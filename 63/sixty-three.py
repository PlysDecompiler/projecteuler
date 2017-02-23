#https://projecteuler.net/problem=63

exp = 1
nums = set()
lastlen = 0
while True:
    curr = 1    
    while True:
        num = curr**exp
        if len(str(num)) == exp:
            nums.add(num)
        elif len(str(num)) > exp:
            break
        curr+=1
    exp+=1
    if lastlen == len(nums):
        break
    lastlen = len(nums)
    
print len(nums)
#solution: 49
