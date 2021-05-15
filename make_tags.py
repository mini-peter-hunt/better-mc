from json import dumps
from os.path import join

from options import get_option


def dump(obj):
    return dumps(obj, indent=2)


tags_path = join('better-mc', 'data', 'minecraft', 'tags')

dirt_tag = [
    'dirt', 'grass_block', 'podzol', 'coarse_dirt', 'mycelium',
]
stone_tag = [
    'cobblestone', 'stone', 'smooth_stone',
    'andesite', 'polished_andesite',
    'diorite', 'polished_diorite',
    'granite', 'polished_granite',

    'sandstone', 'smooth_sandstone',
    'red_sandstone', 'smooth_red_sandstone',

    'netherrack', 'blackstone',
    'basalt', 'polished_basalt', 'smooth_basalt',

    'end_stone',
]
soul_tag = [
    'soul_sand', 'soul_soil',
]
natural_tag = dirt_tag + stone_tag + soul_tag + [
    'sand', 'red_sand', 'gravel', '#logs'
]


def write_enderman_unpickable():
    with open(join(tags_path, 'blocks', f'enderman_holdable.json'), 'w') as file:
        file.write(dump({'replace': False,
                         'values': []}))


def write_mushroom_growable():
    with open(join(tags_path, 'blocks', f'mushroom_grow_block.json'), 'w') as file:
        file.write(dump({'replace': False,
                         'values': dirt_tag}))


def write_stone():
    with open(join(tags_path, 'items', f'stone_crafting_materials.json'), 'w') as file:
        file.write(dump({'replace': False,
                         'values': stone_tag}))
    with open(join(tags_path, 'items', f'stone_tool_materials.json'), 'w') as file:
        file.write(dump({'replace': False,
                         'values': stone_tag}))


def write_natural_soul():
    with open(join(tags_path, 'blocks', f'soul_speed_blocks.json'), 'w') as file:
        file.write(dump({'replace': False,
                         'values': natural_tag}))


def make_tags():
    if get_option('endermanUnpickable'):
        write_enderman_unpickable()
    if get_option('mushroomGrowable'):
        write_mushroom_growable()
    if get_option('variantedStoneRecipe'):
        write_stone()
    if get_option('naturalSoul'):
        write_natural_soul()


if __name__ == '__main__':
    make_tags()
