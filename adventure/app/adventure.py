import json

import states
from commands import *
from helpers import show_room, get_room_by_name
from items import figa, coin, canister, matches, fire_extinguisher, newspaper


def init_game():
    # init game
    with open('world.json', 'r', encoding='utf-8') as file:
        world = json.load(file)

    # post processing
    room = get_room_by_name(world, 'dungeon')
    room['items'].append(canister)
    room['items'].append(matches)
    room['items'].append(fire_extinguisher)
    room['items'].append(newspaper)

    context = {
        'state': states.PLAY,
        'backpack': {
            'items': [],
            'max': 2,
        },
        'history': [],
        'world': world,
        'room': room,  # get_room_by_name(world, 'dungeon'),
        'commands': []
    }

    context['backpack']['items'].append(figa)
    context['backpack']['items'].append(coin)

    return context


if __name__ == '__main__':
    # banner
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print("                       and his Great Escape                        ")
    print()

    context = init_game()
    context['commands'] = [
        cmd_about,
        cmd_inventory,
        cmd_drop,
        cmd_take,
        cmd_examine,
        cmd_quit,
        cmd_look_around,
        cmd_commands,
        cmd_use,
        cmd_west,
        cmd_east,
        cmd_south,
        cmd_north,
        cmd_save,
        cmd_load,
    ]

    # serialization
    # import json
    # file = open('world.json', 'w+', encoding='utf-8')
    # json.dump(context['world'], file, indent=4, ensure_ascii=False)
    # file.close()

    # rendering the dark room
    show_room(context['room'])

    # main loop
    while context['state'] == states.PLAY:
        # normalizing string
        line = input('> ').lower().strip()

        # empty input
        if line == '':
            continue

        command, param = parse(line, context)
        if command is None:
            print('Tak?? pr??kaz nepozn??m.')
        else:
            callback = command['exec']
            callback(context, param)

        # check game win
        if context["room"]["name"] == 'heaven':
            context["state"] = states.WIN
            print('Ke?? si otvoril dvere a pre??iel si nimi do miestnosti na severe, s rados??ou si zistil, ??e si sa '
                  'ocitol pred nebeskou br??nou, kde ??a u?? s ??smevom na per??ch ??akal s??m Sv??t?? Peter s poh??rom '
                  '??ampansk??ho. \nCel?? nate??en?? sa rozbehne?? smerom k nemu a spolu prech??dzate nebeskou br??nou. T??to')
            print("__        __   _ _   ____                   _")
            print("\\ \\      / /__| | | |  _ \\  ___  _ __   ___| |")
            print(" \\ \\ /\\ / / _ \\ | | | | | |/ _ \\| '_ \\ / _ \\ |")
            print("  \\ V  V /  __/ | | | |_| | (_) | | | |  __/_|")
            print("   \\_/\\_/ \\___|_|_| |____/ \\___/|_| |_|\\___(_)")

        if context["room"]["name"] == 'hell':
            context["state"] = states.LOSE
            print('Tvoja p???? touto hrou sa ne????astne, ke?? si vo??iel do nespr??vnych dver??, za ktor??mi sa nach??dzali '
                  'br??n?? pekla. Ke?? si sa oto??il, zistil si, ??e von sa u?? nikdy nedostane??. \nV ??ia??ke vid????, ako si '
                  'na teba Satan ch??st?? svoje vidly. Do??lo ti, ??e si sa dostal do poriadn??ho mal??ru.')

    # game credits
    print('\n(c)2021 by Darius Lindvai')
