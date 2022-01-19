from helpers import get_item_by_name
from .door import SOAKED
from .features import USABLE, MOVABLE


def _use(context: dict):
    # raise NotImplementedError('Usage of this item was not yet implemented.')
    door = get_item_by_name('dvere', context["room"]["items"])
    if door is None:
        print('Vzal si kanister do ruky, trošku si zaposiloval a uľavil si si sprostým slovom. Hneď sa cítiš lepšie.')
        return

    door["description"] = 'Veľké masívne dubové dvere. Len tak niečo a niekto s nimi nepohne, keď sú zamknuté. A to ' \
                          'teda sú. A ešte k tomu aj parádne nasiaknuté vysokooktánovým benzínom.'
    door["state"] = SOAKED
    canister["description"] = 'Veľký 25L kanister. Odšroboval si veko a nadýchol si sa. Ešte pred chvíľou tu bol ' \
                              'určite vysokooktánový benzín. Ale teraz tu už nie je nič.'
    canister["features"].remove(USABLE)

    print('Odšroboval si vrchnák z kanistra, rozohnal si sa a celý jeho obsah si vylial na dubové dvere.')


canister = {
    'name': 'kanister',
    'description': 'Veľký 25L kanister. Odšroboval si veko a nadýchol si sa. Vysokooktánový benzín. Isto zo Slovnaftu.',
    'features': [MOVABLE, USABLE],
    'use': _use
}
