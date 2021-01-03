from clean import clean
from make_itemfunc import make_itemfunc
from make_recipe import make_recipe


def make():
    clean()
    make_itemfunc()
    make_recipe()


if __name__ == '__main__':
    make()
