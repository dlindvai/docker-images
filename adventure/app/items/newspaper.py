from random import choice

from .features import MOVABLE, USABLE

headlines = [
    'Primár z Martina, kde obmedzujú onkologické operácie: Máme viac pacientov ako v druhej vlne. Sú '
    'agresívnejší, majú načítané hlúposti z internetu',
    'Psychiatrička: Deti dnes vyrastajú pod obrovským tlakom. Keď sa im niečo hneď nepodarí, je to pre ne '
    'katastrofa',
    'Starostka Aufrichtová nepôjde do boja o Staré Mesto s koalíciou Vallo – PS – SaS. Súťaž je dobrá, hovorí',
    'Školský týždeň: Je rozdiel byť učiteľom či učiteľkou v Bratislave a na východe'
]


def _use(context: dict) -> None:
    print('Hmmm, vidanie denníka N z novembra 2021, pozrime sa čo píšu...')
    # print(choice(headlines))
    headline = choice(headlines)
    print(headline)

newspaper = {
    'name': 'noviny',
    'description': 'Bravíčko do každej domácnosti.',
    'features': [MOVABLE, USABLE],
    'use': _use
}
