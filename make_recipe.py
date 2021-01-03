from json import dumps
from os.path import join

from const import TOOL_TYPES, ARMOR_TYPES, COLORS
from options import get_option


def dump(obj):
    return dumps(obj, indent=2)


recipe_path = join('better-crafting', 'data', 'minecraft', 'recipes')

smeltables = [
    ('cobblestone', 'stone'),
    ('quartz', 'smooth_quartz'),
    ('red_sandstone', 'smooth_red_sandstone'),
    ('sandstone', 'smooth_sandstone'),
]
smeltable_types = ('slab', 'stairs')

vineables = [
    ('cobblestone', 'mossy_cobblestone'),
    ('stone_brick', 'mossy_stone_brick'),
]
vineable_types = ('slab', 'stairs')

tool_upgradables = [
    ('wooden', 'cobblestone', 'stone'),
    ('stone', 'iron_ingot', 'diamond'),
    ('iron', 'iron', 'diamond'),
]

armor_upgradables = [
    ('lether', 'iron_ingot', 'iron'),
    ('iron', 'diamond', 'diamond'),
]

decraftables = [
    ('blue_ice', 'packed_ice', 9),
    ('nether_wart_block', 'nether_wart', 9),
    ('packed_ice', 'ice', 9),
    ('#wool', 'string', 4),
]

shapelesses = [
    ((('sugar_cane', 3),), 'paper', 3),
    ((('shulker_shell', 2), ('chest', 1)), 'shulker_box', 1),
]


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
                         'ingredient': [
                             {'item': f'minecraft:{material}_{kind}'},
                             {'item': 'minecraft:vine'}],
                         'result': f'minecraft:{result}_{kind}'}))


def write_upgradable_recipes(material, addition, result, kind):
    with open(join(recipe_path,
                   f'{result}_{kind}_smithing.json',), 'w') as file:
        file.write(dump({'type': 'minecraft:smithing',
                         'base': {'item': f'minecraft:{material}_{kind}'},
                         'addition': {'item': f'minecraft:{addition}'},
                         'result': {
                             'item': f'minecraft:{result}_{kind}'}}))


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
    ingredients = [{'item': ingredient[0], 'count': ingredient[1]}
                   for ingredient in ingredients]
    with open(join(recipe_path, f'{result}_shapeless.json'), 'w') as file:
        file.write(dump({'type': 'minecraft:crafting_shapeless',
                         'ingredients': ingredients,
                         'result': {'item': f'minecraft:{result}',
                                    'count': amount}}))


def make_recipe():
    if get_option('smeltableRecipes'):
        for material, result in smeltables:
            for kind in smeltable_types:
                write_smeltable_recipes(material, result, kind)
        write_smeltable_recipes('stone', 'smooth_stone', 'slab')

    if get_option('vineableRecipes'):
        for material, result in vineables:
            for kind in vineable_types:
                write_vineable_recipes(material, result, kind)

    if get_option('upgradableRecipes'):
        for material, addition, result in tool_upgradables:
            for kind in TOOL_TYPES:
                write_upgradable_recipes(material, addition, result, kind)

        for material, addition, result in armor_upgradables:
            for kind in ARMOR_TYPES:
                write_upgradable_recipes(material, addition, result, kind)

    if get_option('decraftableRecipes'):
        for material, result, amount in decraftables:
            write_decraftable_recipes(material, result, amount)

    if get_option('shapelessRecipes'):
        for ingredients, result, amount in shapelesses:
            write_shapeless_recipes(ingredients, result, amount)


if __name__ == '__main__':
    make_recipe()
