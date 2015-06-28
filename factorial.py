fact = lambda n: reduce(lambda x,y:x*y, range(1,n+1)) if n>1 else 1

n = int(raw_input())
if(n<0):
    print "number should be positive"
else:
    print fact(n)
