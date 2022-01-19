from helpers import get_item_by_name
from items import MOVABLE


def _exec(context: dict, param: str):
    backpack = context['backpack']
    room = context['room']

    # if the name was not entered
    if not param:
        print('Neviem, čo chceš vziať.')
        return

    # search for item in room items
    item = get_item_by_name(param, room['items'])

    # item not found
    if item is None:
        print('Taký predmet tu nikde nevidím.')
        return

    # is the item movable?
    if MOVABLE not in item['features']:
        print('Tento predmet sa nedá vziať.')
        return

    # is backpack full?
    if len(backpack['items']) >= backpack['max']:
        print('Batoh je plný')
        return

    # save to history
    context["history"].append(f'{cmd["name"]} {param}')

    # take item
    room['items'].remove(item)
    backpack['items'].append(item)
    print(f'Do batohu si si vložil predmet {param}.')


cmd = {
    'name': "vezmi",
    'description': 'vezme predmet z miestnosti a vloží si ho do batohu',
    'aliases': ("take",),
    'exec': _exec,
}
