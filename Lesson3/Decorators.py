import time
a_string = "This is a global variable"

def countcalls(f):
    def _f(*args):
        callcounts[_f] += 1
        return f(*args)
    callcounts[_f] = 0
    return _f

def memo(f):
    cache = {}
    def inner(*args):
        try:
            return cache[args]
        except KeyError:
            result = cache[args] = f(*args)
            return result
        except TypeError:
            return f(args)
    return inner

@countcalls
@memo
def fib(x):
    if x <= 1:
        return 1
    return fib(x-1) + fib(x-2)

s_time = time.time()
print fib(200)
print "Time:", time.time() - s_time