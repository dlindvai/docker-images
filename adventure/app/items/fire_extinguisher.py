from helpers import get_item_by_name
from .door import BURNING
from .features import MOVABLE, USABLE


def _use(context: dict) -> None:
    # raise NotImplementedError('Usage of this item was not yet implemented.')
    door = get_item_by_name('horiace dvere', context["room"]["items"])
    if door is None and door["state"] != BURNING:
        print('Skontroloval si nálepku a plombu na prístroji. Platnosť do 4.7.1957.')
        return

    context["room"]["items"].remove(door)
    fire_extinguisher["features"].remove(USABLE)
    fire_extinguisher["description"] = 'Prázdny hasiaci prístroj. Užitočný ako ťažidlo na papiere na pracovnom stole.'
    context["room"]["exits"]["east"] = 'garden'

    print('Ako správny požiarnik si neváhal, odstránil si plombu z hasiaceho prístroja a udrel si hlavičku o podlahu, '
          'čím si odstránil poistku. Nasmeroval si hubicu hasiaceho prístroja k dverám a začal si hasiť. \nPlameň sa '
          'pod návalom narastajúcej peny uhasil a pod váhou peny sa dvere rozpadli. Cesta von je voľná. Podskočil si '
          'si od radosti.')


fire_extinguisher = {
    'name': 'hasiaci pristroj',
    'description': 'Červená nádoba snehového hasiaceho prístroja. Plomba dáva vedieť, že ešte nebol použitý.',
    'features': [MOVABLE, USABLE],
    'use': _use
}
