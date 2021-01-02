from json import dumps
from os.path import join


recipe_path = join('better-crafting', 'data', 'minecraft', 'recipes')

smlt_materials = ('cobblestone', 'quartz', 'red_sandstone', 'sandstone')
smlt_results = ('stone', 'smooth_quartz',
                'smooth_red_sandstone', 'smooth_sandstone')
smlt_types = ('slab', 'stairs')

vine_materials = ('cobblestone', 'stone_brick')
vine_results = ('mossy_cobblestone', 'stone_brick')
vine_types = ('slab', 'stairs')

t_upgd_materials = ('wooden', 'stone', 'iron')
t_upgd_addition = ('cobblestone', 'iron_ingot', 'diamond')
t_upgd_results = ('stone', 'iron', 'diamond')
t_upgd_types = ('axe', 'hoe', 'pickaxe', 'shovel', 'sword')

a_upgd_materials = ('leather', 'iron')
a_upgd_addition = ('iron_ingot',  'diamond')
a_upgd_results = ('iron',  'diamond')
a_upgd_types = ('helmet', 'chestplate', 'leggings', 'boots')


def write_smeltable_recipes(s_material, s_result, s_type):
    with open(join(
        recipe_path,
        f'{s_result}_{s_type}_from_smelting.json',
    ), 'w') as file:
        file.write(dumps({'type': 'minecraft:smelting',
                          'ingredient': {
                              'item': f'minecraft:{s_material}_{s_type}'},
                          'result': f'minecraft:{s_result}_{s_type}',
                          'experience': 0.1,
                          'cookingtime': 200}, indent=2))


def write_vineable_recipes(v_material, v_result, v_type):
    with open(join(
        recipe_path,
        f'{v_result}_{v_type}.json',
    ), 'w') as file:
        file.write(dumps({'type': 'minecraft:crafting_shapeless',
                          'ingredient': [
                              {'item': f'minecraft:{v_material}_{v_type}'},
                              {'item': 'minecraft:vine'}],
                          'result': f'minecraft:{v_result}_{v_type}'},
                         indent=2))


def write_upgradable_recipes(u_material, u_addition, u_result, u_type):
    with open(join(
        recipe_path,
        f'{u_result}_{u_type}_smithing.json',
    ), 'w') as file:
        file.write(dumps({"type": "minecraft:smithing",
                          "base": {
                              "item": f"minecraft:{u_material}_{u_type}"
                          },
                          "addition": {"item": f"minecraft:{u_addition}"},
                          "result": {
                              "item": f"minecraft:{u_result}_{u_type}"
                          }},
                         indent=2))


def make_recipe():
    # smeltable recipes
    for m_i, s_material in enumerate(smlt_materials):
        for s_type in smlt_types:
            write_smeltable_recipes(s_material, smlt_results[m_i], s_type)
    write_smeltable_recipes('stone', 'smooth_stone', 'slab')

    # "vineable" recipes
    for m_i, v_material in enumerate(vine_materials):
        for v_type in vine_types:
            write_vineable_recipes(v_material, vine_results[m_i], v_type)
    write_smeltable_recipes('stone', 'smooth_stone', 'slab')

    # upgradable tool recipes
    for m_i, t_material in enumerate(t_upgd_materials):
        for t_type in t_upgd_types:
            write_upgradable_recipes(t_material, t_upgd_addition[m_i],
                                          t_upgd_results[m_i], t_type)

    # upgradable armor recipes
    for m_i, a_material in enumerate(a_upgd_materials):
        for a_type in a_upgd_types:
            write_upgradable_recipes(a_material, a_upgd_addition[m_i],
                                          a_upgd_results[m_i], a_type)


if __name__ == '__main__':
    make_recipe()
