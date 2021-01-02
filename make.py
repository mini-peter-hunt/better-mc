from clean import clean
from make_recipe import make_recipe
from make_itemfunc import make_itemfunc


def make():
    clean()
    make_recipe()
    make_itemfunc()


if __name__ == '__main__':
    make()
