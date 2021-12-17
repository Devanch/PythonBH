a = "Hello"
d = "World"
def concat(*args, reversed=False):
    s = " "
    s = s.join(args)

    if (reversed):
        s = s[::-1]

    return(s)

res1 = concat(a,d,a,d, "gogo", "momo", reversed=True)
res2 = concat(a,d,a,d, "gogo", "momo", reversed=False)
res3 = concat(a,d,a,d, "gogo", "momo")

print(res1)
print(res2)
print(res3)
        # for item in args:
        #     s += item