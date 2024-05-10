def recursive_fibonacci(n):
    if n <= 1:
        print("inside one",n)
        return n
    else:
        print("N: =", n)  # 5
        # print(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
        return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))
        # 0+
        # 2+1


x = recursive_fibonacci(4)
print(x)