# fibonacci = (a+b)-a
def fib_func(n):
    p = 0
    c = 1
    for i in range(n):
        print(c)
        p, c = c, c+p
    
def fib_gen(n):
    p, c = 0, 1
    for i in range(n):
        yield c
        p, c = c, c+p
        

for n in fib_gen(5): 
    print(n)

print('\n')

fib_func(10)