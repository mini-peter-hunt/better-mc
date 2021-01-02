from clean import clean
from tool_gen import tool_gen


def gen():
    clean()
    tool_gen()


if __name__ == '__main__':
    gen()
