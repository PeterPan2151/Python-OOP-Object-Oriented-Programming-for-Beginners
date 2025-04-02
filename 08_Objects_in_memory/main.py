print(object)

print(isinstance(5, object))
print(isinstance([1, 2, 3, 4], object))

print(isinstance((1, 2, 3, 4), object))
print(isinstance('Hello World', object))

def f(x):
    return x

print(isinstance(f, object))
