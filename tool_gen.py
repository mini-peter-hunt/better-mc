from os.path import join


func_path = join('better-crafting', 'data', 'minecraft',
                 'functions', 'better_crafting')

tool_materials = ('wooden', 'stone', 'iron', 'golden', 'diamond', 'netherite')
tool_types = ('axe', 'hoe', 'pickaxe', 'shovel', 'sword')
tm_ids = ('wdn', 'stn', 'irn', 'gldn', 'dmnd', 'nthrt')
tt_ids = ('axe', 'hoe', 'pckx', 'shvl', 'swrd')

extra_tool = ('bow', 'carrot_on_a_stick', 'crossbow', 'fishing_rod',
              'flint_and_steel', 'shears', 'shield', 'trident',
              'warped_fungus_on_a_stick')
te_ids = ('bow', 'croask', 'csbw', 'fsrd', 'fltst',
          'shrs', 'shld', 'trdt', 'fgoask')

armor_materials = ('leather', 'chainmail', 'iron',
                   'golden', 'diamond', 'netherite')
armor_types = ('helmet', 'chestplate', 'leggings', 'boots')
am_ids = ('lthr', 'chnml', 'irn', 'gldn', 'dmnd', 'nthrt')
at_ids = ('hlmt', 'chsplt', 'lgns', 'bts')

extra_armor = ('elytra', 'turtle_helmet')
ae_ids = ('eltr', 'tthm')


def tool_gen():
    init = open(join(func_path, 'init.mcfunction'), 'w')
    tick = open(join(func_path, 'tick.mcfunction'), 'w')

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
                f'tag: {{Unbreakable: 1b}}}}]}}] '
                f'run scoreboard players set @s '
                f'has_{short_id} 1\n'
                f'execute as @a[scores={{has_{short_id}=1}}] '
                f'run clear @s minecraft:{item_id} 1\n'
                f'execute as @a[scores={{has_{short_id}=1}}] '
                f'run give @s minecraft:{item_id}{{Unbreakable:1}} 1\n'
                f'execute as @a[scores={{has_{short_id}=1}}] '
                f'run scoreboard players set @s '
                f'has_{short_id} 0\n'
            )

    for m_i, t_material in enumerate(tool_materials):
        comment(f'{t_material.capitalize()} Tools', init, tick)
        for t_i, t_type in enumerate(tool_types):
            process(f'{t_material}_{t_type}', f'{tm_ids[m_i]}_{tt_ids[t_i]}')

    comment('Extra Tools', init, tick)
    for index, tool in enumerate(extra_tool):
        process(tool, te_ids[index])

    for m_i, a_material in enumerate(armor_materials):
        comment(f'{a_material.capitalize()} Armor Pieces', init, tick)
        for t_i, a_type in enumerate(armor_types):
            process(f'{a_material}_{a_type}', f'{am_ids[m_i]}_{at_ids[t_i]}')

    comment('Extra Armor', init, tick)
    for index, tool in enumerate(extra_tool):
        process(tool, te_ids[index])

    init.close()
    tick.close()


if __name__ == '__main__':
    tool_gen()
