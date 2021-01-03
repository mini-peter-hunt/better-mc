from os.path import join

from const import TOOL_TYPES, ARMOR_TYPES
from options import get_option


func_path = join('better-crafting', 'data', 'minecraft',
                 'functions', 'better_crafting')

tool_materials = ('wooden', 'stone', 'iron', 'golden', 'diamond', 'netherite')
tm_ids = ('wdn', 'stn', 'irn', 'gldn', 'dmnd', 'nthrt')
tt_ids = ('axe', 'hoe', 'pckx', 'shvl', 'swrd')

extra_tool = ('bow', 'carrot_on_a_stick', 'crossbow', 'fishing_rod',
              'flint_and_steel', 'shears', 'shield', 'trident',
              'warped_fungus_on_a_stick')
te_ids = ('bow', 'croask', 'csbw', 'fsrd', 'fltst',
          'shrs', 'shld', 'trdt', 'fgoask')

armor_materials = ('leather', 'chainmail', 'iron',
                   'golden', 'diamond', 'netherite')
am_ids = ('lthr', 'chnml', 'irn', 'gldn', 'dmnd', 'nthrt')
at_ids = ('hlmt', 'chsplt', 'lgns', 'bts')

extra_armor = ('elytra', 'turtle_helmet')
ae_ids = ('eltr', 'tthm')


def make_unbreakable_item():
    init = open(join(func_path, 'init.mcfunction'), 'a')
    tick = open(join(func_path, 'tick.mcfunction'), 'a')

    def comment(comment: str, *files):
        for file in files:
            file.write(f'# {comment.strip()}\n')

    def process(item_id, short_id):
        init.write(f'scoreboard players set * '
                   f'has_{short_id} 0\n')
        tick.write(f'function better_crafting/ck_{short_id}\n')
        write_func(item_id, short_id)

    def write_func(item_id, short_id):
        with open(join(func_path, f'ck_{short_id}.mcfunction'),
                  'w') as checker:
            checker.write(
                f'execute as '
                f'@a[nbt={{Inventory: [{{id: "minecraft:{item_id}", '
                f'tag: {{Unbreakable: 0b}}}}]}}] '
                f'run scoreboard players set @s '
                f'has_{short_id} 1\n'
                f'execute as @a[scores={{has_{short_id}=1}}] '
                f'run clear @s minecraft:{item_id} 1\n'
                f'execute as @a[scores={{has_{short_id}=1}}] '
                f'run give @s '
                f'minecraft:{item_id}{{Damage:0,Unbreakable:1b}} 1\n'
                f'execute as @a[scores={{has_{short_id}=1}}] '
                f'run scoreboard players set @s '
                f'has_{short_id} 0\n'
            )

    for m_i, t_material in enumerate(tool_materials):
        comment(f'{t_material.capitalize()} Tools', init, tick)
        for t_i, t_type in enumerate(TOOL_TYPES):
            process(f'{t_material}_{t_type}', f'{tm_ids[m_i]}_{tt_ids[t_i]}')

    comment('Extra Tools', init, tick)
    for index, tool in enumerate(extra_tool):
        process(tool, te_ids[index])

    for m_i, a_material in enumerate(armor_materials):
        comment(f'{a_material.capitalize()} Armor Pieces', init, tick)
        for t_i, a_type in enumerate(ARMOR_TYPES):
            process(f'{a_material}_{a_type}', f'{am_ids[m_i]}_{at_ids[t_i]}')

    comment('Extra Armor', init, tick)
    for index, tool in enumerate(extra_tool):
        process(tool, te_ids[index])

    init.close()
    tick.close()


def make_itemfunc():
    if get_option('unbreakableItem'):
        make_unbreakable_item()


if __name__ == '__main__':
    make_itemfunc()
