#https://projecteuler.net/problem=12
import threading
from Queue import Queue
import math


def count_divisors(n):
    d = 0
    i = 1
    rt = int(math.sqrt(n))
    while i<rt:
        if n%i == 0:
            d+=1
        i+=1
    d*=2    
    if 1.*n/rt == rt:
        d+=1
    return d

maxi = []
max_lock = threading.Lock()
print_lock = threading.Lock()

def calc(worker):
    j = worker
    ct = count_divisors((j*(j+1))/2 )
    if ct > 500:
        with max_lock:
            maxi.append((j,(j*(j+1))/2,ct))

q = Queue()

def threader():
    while True:
        worker = q.get()
        calc(worker)
        q.task_done()

for x in range(500):
    t = threading.Thread(target = threader)

    t.daemon = True
    t.start()

worker = 1
while True:
    with max_lock:
        if len(maxi):
            break
    q.put(worker)
    worker+=1
    if worker % 500 == 0:
        print "hello", worker

q.join()

print maxi
#(12375, 76576500, 576)


