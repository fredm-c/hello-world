def greet(name, message="Hello"):
    """Return a greeting string."""
    return f"{message}, {name}!"


if __name__ == "__main__":
    print(greet("World"))
