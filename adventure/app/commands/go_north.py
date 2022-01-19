from helpers import show_room, get_room_by_name


def _exec(context: dict, param: str):
    room = context["room"]["exits"]["north"]
    if room is None:
        print('Tam sa nedá ísť.')
    else:
        # save to history
        context["history"].append(f'{cmd["name"]}')

        # go north
        print('Kráčaš na sever.')
        context["room"] = get_room_by_name(context['world'], room)
        show_room(context['room'])


cmd = {
    'name': 'sever',
    'description': 'presunie sa do miestnosti na sever, ak sa tým smerom dá ísť',
    'aliases': ('chod na sever', 'go north'),
    'exec': _exec
}
