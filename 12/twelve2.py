#https://projecteuler.net/problem=12
import threading
from Queue import Queue

def count_divisors(n):
    d = 0
    i = 1
    while i<=n/2+1:
        if n%i == 0:
            d+=1
        i+=1
    d+=1
    return d

print_lock = threading.Lock()

def calc(worker):
    j = worker
    ct = count_divisors((j*(j+1))/2 )
    with print_lock:
        print worker, ct

q = Queue()

def threader():
    while True:
        worker = q.get()
        calc(worker)
        q.task_done()

for x in range(50):
    t = threading.Thread(target = threader)

    t.daemon = True
    t.start()

for worker in range(6900,7000):
    q.put(worker)

q.join()

