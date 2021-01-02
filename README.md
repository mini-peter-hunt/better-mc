# Better Crafting

<p align="center">
  <img src="https://img.shields.io/github/stars/mini-peter-hunt/better-crafting">
  <img src="https://img.shields.io/static/v1?label=Contributions&message=Welcome&color=0059b3">
  <img src="https://img.shields.io/github/repo-size/mini-peter-hunt/better-crafting">
  <img src="https://img.shields.io/github/languages/top/mini-peter-hunt/better-crafting">
  <img src="https://img.shields.io/github/license/mini-peter-hunt/better-crafting">
</p>

A data pack that change Minecraft, not limited to crafting!
Contains easier tool, weapon and armor usage. There are even more options in the same style in the description below.

## Installation

To generate the full content, use the following command:

```
python3 make.py
```

You can adjust to only generate the content you want in the `make.py`

And to clean up the generated content, use the following command:

```
python3 clean.py
```

Add this data pack to a exist world:

- Go to your `.minecraft` folder, go to `saves` and enter the world you want this data pack installed.
- Go to `datapacks` and copy the `better-crafting` folder inside the project folder into the `datapacks`
- Run the game and use the command `/reload` to load the added data packs.

Or generate a world with this data pack. (started from 1.16 Pre-release 1)

This project requires Python 3.6+

## More ingredients

For more options in the style of this data pack, here's some things you can try:

- Modify some gamerule:
- - Set `doFireTick` to `false`
- - Set `doWeatherCycle` to `false`
- - Set `keepInventory` to `true`
- - Set `mobGriefing` to `false`
- - Set `randomTickSpeed` to `300`
- Use [Vanilla Tweaks](http://vanillatweaks.net/)
- Use [Quark Mod](https://quark.vazkii.net/)

## Current State

The features that are currently implemented are as follows:

- Mend everything in the inventory and make them unbreakable
- Make productions (slabs and stairs) smeltable and "vineable" (if has the original recipe)
- Make tools and armor pieces cheaply upgradable using smithing table (wooden/leather -> iron -> diamond)

## Known Issues

- Mending a thing and making it unbreakable removes all NBT tags but `Unbreakable`
- Upgrading a tool or a armor piece may remove its NBT tags.

## Donation

This project is open-source and free-to-use, it would be really helpful to support me!
For more information, please see my [Patreon](https://patreon.com/that_peterhunt).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](LICENSE.txt)
