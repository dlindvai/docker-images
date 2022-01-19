from helpers import show_room, get_room_by_name


def _exec(context: dict, param: str):
    room = context["room"]["exits"]["south"]
    if room is None:
        print('Tam sa nedá ísť.')
    else:
        # save to history
        context["history"].append(f'{cmd["name"]}')

        # go south
        print('Kráčaš na juh.')
        context["room"] = get_room_by_name(context['world'], room)
        show_room(context['room'])


cmd = {
    'name': 'juh',
    'description': 'presunie sa do miestnosti na juh, ak sa tým smerom dá ísť',
    'aliases': ('chod na juh', 'go south'),
    'exec': _exec
}
