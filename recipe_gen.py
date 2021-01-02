from json import dumps
from os.path import join


recipe_path = join('better-crafting', 'data', 'minecraft', 'recipes')

smlt_materials = ('cobblestone', 'quartz', 'red_sandstone', 'sandstone')
smlt_prods = ('stone', 'smooth_quartz',
              'smooth_red_sandstone', 'smooth_sandstone')
smlt_types = ('slab', 'stairs')

vine_materials = ('cobblestone', 'stone_brick')
vine_prods = ('mossy_cobblestone', 'stone_brick')
vine_types = ('slab', 'stairs')


def write_recipe_for_smeltable(s_material, s_production, s_type):
    with open(join(
        recipe_path,
        f'{s_production}_{s_type}_from_smelting.json',
    ), 'w') as file:
        file.write(dumps({'type': 'minecraft:smelting',
                          'ingredient': {
                              'item': f'minecraft:{s_material}_{s_type}'},
                          'result': f'minecraft:{s_production}_{s_type}',
                          'experience': 0.1,
                          'cookingtime': 200}, indent=2))


def write_recipe_for_vineable(v_material, v_production, v_type):
    with open(join(
        recipe_path,
        f'{v_production}_{v_type}.json',
    ), 'w') as file:
        file.write(dumps({'type': 'minecraft:crafting_shapeless',
                          'ingredient': [
                              {'item': f'minecraft:{v_material}_{v_type}'},
                              {'item': 'minecraft:vine'}],
                          'result': f'minecraft:{v_production}_{v_type}'},
                         indent=2))


def recipe_gen():
    # smeltable productions
    for m_i, s_material in enumerate(smlt_materials):
        for s_type in smlt_types:
            write_recipe_for_smeltable(s_material, smlt_prods[m_i], s_type)
    write_recipe_for_smeltable('stone', 'smooth_stone', 'slab')

    # "vineable" productions
    for m_i, v_material in enumerate(vine_materials):
        for v_type in vine_types:
            write_recipe_for_vineable(v_material, vine_prods[m_i], v_type)


if __name__ == '__main__':
    recipe_gen()
