from items import canister, matches, fire_extinguisher, newspaper, door


world = [
    {
        'name': 'dungeon',
        'description': 'Nachádzaš sa v tmavej zatuchnutej miestnosti. Na kamenných stenách sa nenachádza žiadne okno, '
                       'čo dáva tušiť, že si niekoľko metrov pod zemou. Žeby košický hrad? Aj to je možné, ti '
                       'prebleslo hlavou.',
        'items': [
            canister,
            matches,
            fire_extinguisher,
            newspaper,
            door
        ],
        'exits': {
            'west': None,
            'south': None,
            'north': None,
            'east': None
        }
    },

    {
        'name': 'garden',
        'description': 'Značne neudržiavaný priestor, ktorý sa určite pred pár rokmi volal záhradka.',
        'items': [],
        'exits': {
            'west': 'dungeon',
            'south': 'hell',
            'north': 'heaven',
            'east': None
        }
    },

    {
        'name': 'heaven',
        'description': 'Prichádzaš ku nebu. Svätý Peter ťa už čaká pri nebeskej bráne. ',
        'items': [],
        'exits': {
            'west': None,
            'south': 'garden',
            'north': None,
            'east': None
        }
    },

    {
        'name': 'hell',
        'description': 'Pekelné peklo a nič viac. Satan si už na teba chystá svoje vidly.',
        'items': [],
        'exits': {
            'west': None,
            'south': None,
            'north': None,
            'east': None
        }
    },
]
