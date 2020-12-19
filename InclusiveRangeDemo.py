def inclusiveRange(n):
    for i in range(n + 1):
        yield i 

x = inclusiveRange(5)
stop = False
while not stop:
    try:
        print(next(x))
    except StopIteration:
        stop = True
        print("done!")


arr=[0,1,2,3,4,5]
start = len(arr)
stop = 3
step = -1

[print(arr[:i]) for i in range(start,stop,step)]



    
