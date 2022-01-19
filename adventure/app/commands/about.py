def _exec(context: dict, param: str):
    print('Ďalšie veľké dobrodružstvo Indiana Jonesa. Tentokrát zápasí s jazykom Python v tmavej miestnosti.')


cmd = {
    'name': 'o hre',
    'description': 'zobrazí informácie o hre',
    'aliases': ('about', 'info', '?'),
    'exec': _exec,
}
