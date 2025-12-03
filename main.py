def function_1(x: int, y: int) -> int:
    return x + y


def function_2(x: int, y: int) -> int:
    return x - y


def print_file(path: str) -> str:
    try:
        with open(path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "The file 'my_text_file.txt' was not found."


def useful_function(x: int, y: int) -> int:
    return x + y - y


if __name__ == "__main__":
    x = 10
    y = 25
    t = function_1(x, y)
    print(t)
    t = function_2(x, y)
    print(t)
    msg = print_file("./input.txt")
    print(msg)
    t = useful_function(x, y)
    print(t)
