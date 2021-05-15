from os.path import join
from os import remove, walk


def clean():
    recipe_path = join('better-mc', 'data', 'minecraft', 'recipes')

    for path in [*walk(recipe_path)][0][2]:
        remove(join(recipe_path, path))

    block_tags = join('better-mc', 'data', 'minecraft', 'tags', 'blocks')

    for path in [*walk(block_tags)][0][2]:
        remove(join(block_tags, path))


if __name__ == '__main__':
    clean()
