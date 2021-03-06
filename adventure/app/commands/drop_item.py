from helpers import get_item_by_name


def _exec(context: dict, param: str):
    backpack = context['backpack']
    room = context['room']

    # if the name was not entered
    if not param:
        print('Neviem, čo chceš položiť.')
        return

    # search for item in backpack items
    item = get_item_by_name(param, backpack['items'])

    # item not found
    if item is None:
        print('Taký predmet pri sebe nemáš.')
        return

    # save to history
    context["history"].append(f'{cmd["name"]} {param}')

    # drop item
    backpack['items'].remove(item)
    room['items'].append(item)
    print(f'Do miestnosti si položil predmet {param}.')


cmd = {
    'name': "poloz",
    'description': 'položí zvolený predmet v miestnosti',
    'aliases': ("drop",),
    'exec': _exec,
}
