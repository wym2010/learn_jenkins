def fib():
        x,y=0,1
        while 1:
                yield x
                x,y=y,x+y
for i in range(0,10):
        print (fib().__next__())
