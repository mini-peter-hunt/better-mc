from clean import clean
from recipe_gen import recipe_gen
from tool_gen import tool_gen


def make():
    clean()
    recipe_gen()
    tool_gen()


if __name__ == '__main__':
    make()
