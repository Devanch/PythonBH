a = "Hello"
d = "World"

def decorator(func):
    def inspect(*args, **kwargs):
        print(args)
        print(kwargs)

        print(func(*args))
    return(inspect)


def concat(*args, reversed=False):
    s = " "
    s = s.join(args)

    if (reversed):
        s = s[::-1]

    return(s)

concat = decorator(concat)
concat(a,d,a,d, "gogo", "momo", reversed=True)
concat(a,d,a,d, "gogo", "momo", reversed=False)
concat(a,d,a,d, "gogo", "momo")
