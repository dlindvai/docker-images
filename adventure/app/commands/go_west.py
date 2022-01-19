from helpers import show_room, get_room_by_name


def _exec(context: dict, param: str):
    room = context["room"]["exits"]["west"]
    if room is None:
        print('Tam sa nedá ísť.')
    else:
        # save to history
        context["history"].append(f'{cmd["name"]}')

        # go west
        print('Kráčaš na západ.')
        context["room"] = get_room_by_name(context['world'], room)
        show_room(context['room'])


cmd = {
    'name': 'zapad',
    'description': 'presunie sa do miestnosti na zapad, ak sa tým smerom dá ísť',
    'aliases': ('chod na zapad', 'go west'),
    'exec': _exec
}
