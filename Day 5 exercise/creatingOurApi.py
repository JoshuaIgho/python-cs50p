def main():
    hello("world")
    goodbye("james")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

#main() to make it work as a api, we will have to remove main()