from json import dumps
from os.path import join

from const import (
    TOOL_TYPES, ARMOR_TYPES,
    TREE_TYPES, MUSHROOM_TYPES, FUNGUS_TYPES, FUNGUS_BLOCK_TYPES,
    ORES, MINERALS, SMELTED_MINERALS, COLORS)
from options import get_option


def dump(obj):
    return dumps(obj, indent=2)


recipe_path = join('better-mc', 'data', 'minecraft', 'recipes')

smeltables = [
    ('cobblestone', 'stone'),
    ('quartz', 'smooth_quartz'),
    ('red_sandstone', 'smooth_red_sandstone'),
    ('sandstone', 'smooth_sandstone')]
smeltable_types = ('slab', 'stairs')

vineables = [
    ('cobblestone', 'mossy_cobblestone'),
    ('stone_brick', 'mossy_stone_brick')]
vineable_types = ('slab', 'stairs', 'wall')

tool_upgradables = [
    ('wooden', 'cobblestone', 'stone'),
    ('stone', 'iron_ingot', 'diamond'),
    ('iron', 'diamond', 'diamond')]

armor_upgradables = [
    ('leather', 'iron_ingot', 'iron'),
    ('iron', 'diamond', 'diamond')]

decraftables = [
    ('blue_ice', 'packed_ice', 9),
    ('nether_wart_block', 'nether_wart', 9),
    ('packed_ice', 'ice', 9),
    ('#wool', 'string', 4)]

shapelesses = [
    ((('sugar_cane', 3),), 'paper', 3),
    ((('shulker_shell', 2), ('chest', 1)), 'shulker_box', 1)]

saplings = []

for tree in TREE_TYPES:
    saplings.append((f'{tree}_leaves', f'{tree}_sapling'))

for mushroom in MUSHROOM_TYPES:
    saplings.append((f'{mushroom}_mushroom_block',
                     f'{mushroom}_mushroom'))

for fungus, fungus_block in zip(FUNGUS_TYPES, FUNGUS_BLOCK_TYPES):
    saplings.append((f'{fungus_block}_wart_block', f'{fungus}_fungus'))

ores = []

for block, item in zip(ORES, MINERALS):
    if block in {'redstone_ore', 'lapis_ore'}:
        ores.append((item, block, 'stone', ['#O#', 'O#O', '#O#']))
    elif block == 'gilded_blackstone':
        ores.append((item, block, 'blackstone', ['###', '#O#', '###']))
    elif block == 'nether_gold_ore':
        ores.append((item, block, 'netherrack', ['#O#', 'O#O', '#O#']))
    elif block in {'ancient_debris', 'nether_quartz_ore'}:
        ores.append((item, block, 'netherrack', ['###', '#O#', '###']))
    else:
        ores.append((item, block, 'stone', ['###', '#O#', '###']))


def write_smeltable_recipes(material, result, kind):
    with open(join(recipe_path,
                   f'{result}_{kind}_from_smelting.json'), 'w') as file:
        file.write(dump({'type': 'minecraft:smelting',
                         'ingredient': {
                             'item': f'minecraft:{material}_{kind}'},
                         'result': f'minecraft:{result}_{kind}',
                         'experience': 0.1,
                         'cookingtime': 200}))


def write_vineable_recipes(material, result, kind):
    with open(join(recipe_path, f'{result}_{kind}.json'), 'w') as file:
        file.write(dump({'type': 'minecraft:crafting_shapeless',
                         'ingredients': [
                             {'item': f'minecraft:{material}_{kind}'},
                             {'item': 'minecraft:vine'}],
                         'result': {'item': f'minecraft:{result}_{kind}'}}))


def write_upgradable_recipes(material, addition, result, kind):
    with open(join(recipe_path,
                   f'{result}_{kind}_smithing.json',), 'w') as file:
        file.write(dump({'type': 'minecraft:smithing',
                         'base': {'item': f'minecraft:{material}_{kind}'},
                         'addition': {'item': f'minecraft:{addition}'},
                         'result': {'item': f'minecraft:{result}_{kind}'}}))


def write_decraftable_recipes(material, result, amount):
    if material.startswith('#'):
        material = material[1:]
        ingredients = [{'tag': f'minecraft:{material}'}]
    else:
        ingredients = [{'item': f'minecraft:{material}'}]
    with open(join(recipe_path,
                   f'{result}_from_{material}.json'), 'w') as file:
        file.write(dump({'type': 'minecraft:crafting_shapeless',
                         'ingredients': ingredients,
                         'result': {'item': f'minecraft:{result}',
                                    'count': amount}}))


def write_shapeless_recipes(ingredients, result, amount):
    ingredients = [{'item': f'minecraft:{ingredient[0]}',
                    'count': ingredient[1]}
                   for ingredient in ingredients]
    with open(join(recipe_path, f'{result}_shapeless.json'), 'w') as file:
        file.write(dump({'type': 'minecraft:crafting_shapeless',
                         'ingredients': ingredients,
                         'result': {'item': f'minecraft:{result}',
                                    'count': amount}}))


def write_sapling_recipes(material, result):
    with open(join(recipe_path, f'{result}.json'), 'w') as file:
        file.write(dump({'type': 'minecraft:crafting_shapeless',
                         'ingredients': [{'item': f'minecraft:{material}'}],
                         'result': {'item': f'minecraft:{result}'}}))


def write_ore_recipes(material, result, stone, pattern):
    with open(join(recipe_path, f'{result}.json'), 'w') as file:
        file.write(dump({'type': 'minecraft:crafting_shaped',
                         'pattern': pattern,
                         'key': {'#': {'item': f'minecraft:{stone}'},
                                 'O': {'item': f'minecraft:{material}'}},
                         'result': {'item': f'minecraft:{result}'}}))


def write_better_smelting_ore_recipes(material, result):
    with open(join(recipe_path,
                   f'{result}_from_{material}_with_coal.json'), 'w') as file:
        file.write(dump({'type': 'minecraft:crafting_shaped',
                         'pattern': ['OOO', 'O#O', 'OOO'],
                         'key': {'#': {'item': f'minecraft:coal'},
                                 'O': {'item': f'minecraft:{material}'}},
                         'result': {'item': f'minecraft:{result}',
                                    'count': 16}}))


def make_recipe():
    if get_option('smeltableProducts'):
        for material, result in smeltables:
            for kind in smeltable_types:
                write_smeltable_recipes(material, result, kind)
        write_smeltable_recipes('stone', 'smooth_stone', 'slab')

    if get_option('vineableProducts'):
        for material, result in vineables:
            for kind in vineable_types:
                write_vineable_recipes(material, result, kind)

    if get_option('upgradableTools'):
        for material, addition, result in tool_upgradables:
            for kind in TOOL_TYPES:
                write_upgradable_recipes(material, addition, result, kind)

        for material, addition, result in armor_upgradables:
            for kind in ARMOR_TYPES:
                write_upgradable_recipes(material, addition, result, kind)

    if get_option('decraftableProducts'):
        for material, result, amount in decraftables:
            write_decraftable_recipes(material, result, amount)

    if get_option('shapelessRecipes'):
        for ingredients, result, amount in shapelesses:
            write_shapeless_recipes(ingredients, result, amount)

    if get_option('craftableSaplings'):
        for material, result in saplings:
            write_sapling_recipes(material, result)

    if get_option('craftableOres'):
        for material, result, stone, pattern in ores:
            write_ore_recipes(material, result, stone, pattern)

    if get_option('betterSmeltingOres'):
        for material, result in zip(ORES, SMELTED_MINERALS):
            write_better_smelting_ore_recipes(material, result)


if __name__ == '__main__':
    make_recipe()
