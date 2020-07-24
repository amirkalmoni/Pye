def announce(f):
    def wrapper():
        print("program is starting")
        f()
        print("progra has ended")
    return wrapper

@announce

def hello():
    print("hello world")
hello()
