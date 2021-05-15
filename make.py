from clean import clean
from make_recipe import make_recipe
from make_tags import make_tags


def make():
    clean()
    make_recipe()
    make_tags()


if __name__ == '__main__':
    make()
