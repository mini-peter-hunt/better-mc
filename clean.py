from os.path import join
from os import remove, walk


def clean():
    func_path = join('better-crafting', 'data', 'minecraft',
                     'functions', 'better_crafting')

    for path in [*walk(func_path)][0][2]:
        remove(join(func_path, path))

    recipe_path = join('better-crafting', 'data', 'minecraft', 'recipes')

    for path in [*walk(recipe_path)][0][2]:
        remove(join(recipe_path, path))

    with open(join(func_path, 'tick.mcfunction'), 'w') as file:
        file.write('')


if __name__ == '__main__':
    clean()
