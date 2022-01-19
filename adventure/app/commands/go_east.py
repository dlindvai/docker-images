from helpers import show_room, get_room_by_name


def _exec(context: dict, param: str):
    room = context["room"]["exits"]["east"]
    if room is None:
        print('Tam sa nedá ísť.')
    else:
        # save to history
        context["history"].append(f'{cmd["name"]}')

        # go east
        print('Kráčaš na východ.')
        context["room"] = get_room_by_name(context['world'], room)
        show_room(context['room'])


cmd = {
    'name': 'vychod',
    'description': 'presunie sa do miestnosti na vychod, ak sa tým smerom dá ísť',
    'aliases': ('chod na vychod', 'go east'),
    'exec': _exec
}
