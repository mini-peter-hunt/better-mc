from os.path import join

from const import TOOL_TYPES, ARMOR_TYPES, TOOL_MATERIALS, ARMOR_MATERIALS
from options import get_option


func_path = join('better-crafting', 'data', 'better_crafting', 'functions')

tool_material_shorteneds = ('wdn', 'stn', 'irn', 'gldn', 'dmnd', 'nthr')
tool_type_shorteneds = ('axe', 'hoe', 'pckx', 'shvl', 'swrd')

extra_tool_types = ('bow', 'carrot_on_a_stick', 'crossbow', 'fishing_rod',
                    'flint_and_steel', 'shears', 'shield', 'trident',
                    'warped_fungus_on_a_stick')
extra_tool_shorteneds = ('bow', 'ctsk', 'csbw', 'fsrd', 'flst',
                         'shrs', 'shld', 'trdt', 'fgsk')

armor_material_shorteneds = ('lthr', 'chnml', 'irn', 'gldn', 'dmnd', 'nthr')
armor_type_shorteneds = ('hlmt', 'cspl', 'lgns', 'bts')

extra_armor_types = ('elytra', 'turtle_helmet')
extra_armor_shorteneds = ('eltr', 'tthm')


def make_unbreakable_item():
    init = open(join(func_path, 'init.mcfunction'), 'a')
    tick = open(join(func_path, 'tick.mcfunction'), 'a')

    def comment(comment: str, *files):
        for file in files:
            file.write(f'# {comment.strip()}\n')

    def process(name, shortened):
        init.write(f'scoreboard players set * '
                   f'has_{shortened} 0\n')
        tick.write(f'function better_crafting/ck_{shortened}\n')
        write_func(name, shortened)

    def write_func(name, shortened):
        with open(join(func_path, f'ck_{shortened}.mcfunction'),
                  'w') as checker:
            checker.write(
                f'execute as @a[nbt={{Inventory: [{{id: "minecraft:{name}", '
                f'tag: {{Unbreakable: 0b}}}}]}}] '
                f'run scoreboard players set @s has_{shortened} 1\n'

                f'execute as @a[scores={{has_{shortened}=1}}] '
                f'run clear @s minecraft:{name} 1\n'

                f'execute as @a[scores={{has_{shortened}=1}}] '
                f'run give @s '
                f'minecraft:{name}{{Damage:0,Unbreakable:1b}} 1\n'

                f'execute as @a[scores={{has_{shortened}=1}}] '
                f'run scoreboard players set @s has_{shortened} 0\n')

    for material, shortened_material in zip(
            TOOL_MATERIALS, tool_material_shorteneds):
        comment(f'{material.capitalize()} Tools', init, tick)
        for kind, shortened_kind in zip(
                TOOL_TYPES, tool_type_shorteneds):
            process(f'{material}_{kind}',
                    f'{shortened_material}_{shortened_kind}')

    comment('Extra Tools', init, tick)
    for kind, shortened_kind in zip(extra_tool_types, extra_tool_shorteneds):
        process(kind, shortened_kind)

    for material, shortened_material in zip(
            ARMOR_MATERIALS, armor_material_shorteneds):
        comment(f'{material.capitalize()} Armor Pieces', init, tick)
        for kind, shortened_kind in zip(
                ARMOR_TYPES, armor_type_shorteneds):
            process(f'{material}_{kind}',
                    f'{shortened_material}_{shortened_kind}')

    comment('Extra Armor', init, tick)
    for kind, shortened_kind in zip(extra_armor_types, extra_armor_shorteneds):
        process(kind, shortened_kind)

    init.close()
    tick.close()


def make_itemfunc():
    if get_option('unbreakableItem'):
        make_unbreakable_item()


if __name__ == '__main__':
    make_itemfunc()
