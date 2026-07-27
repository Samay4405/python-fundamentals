x = "global"  # Global variable

def outer():
    x = "enclosed"  # Enclosed variable

    def inner():
        x = "local"  # Local variable
        print(x)  # Local scope is searched first

    inner()

outer()  # Output: "local"
