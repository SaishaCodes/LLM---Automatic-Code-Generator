# legacy.py
def calculate(x, y):
    # Old Python 2 style print and logic
    print "Calculating results for:", x, y
    res = x * y
    if res > 100:
        print "Result is large: %s" % res
    return res

def greet(name):
    print "Hello, %s" % name