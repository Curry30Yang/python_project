def external():
    x = 10
    def internal():
        nonlocal x
        x += 1
        print(x)
    internal()

external()