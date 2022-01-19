from helpers import get_item_by_name
from .door import BURNING, SOAKED
from .features import MOVABLE, USABLE


def _use(context: dict) -> None:
    # raise NotImplementedError('Usage of this item was not yet implemented.')
    door = get_item_by_name('dvere', context["room"]["items"])
    if door is None or door["state"] != SOAKED:
        print('Vzal si do ruky zápalky a prezrel si si ich. Stále su len tri.')
        return

    door["description"] = 'Veľké masívne dubové dvere zachvátené obrovským výdatným plameňom.'
    door["state"] = BURNING
    door["name"] = 'horiace dvere'
    matches["features"].remove(USABLE)
    matches["description"] = 'Pozeráš sa na prázdnu škatuľku zápaliek.'

    print('Škrtol si zápalkou a priložil si ju k nasiaknutým masívnym dubovým dverám. Tie okamžite vzplanuli '
          'obrovským plameňom. ')


matches = {
    'name': 'zapalky',
    'description': 'Safety match zápalky. Zahrkal si krabičkou a po jej otvorení si našiel len tri.',
    'features': [MOVABLE, USABLE],
    'use': _use
}
