from .quit import cmd as cmd_quit
from .about import cmd as cmd_about
from .list_of_commands import cmd as cmd_commands
from .look_around import cmd as cmd_look_around
from .inventory import cmd as cmd_inventory
from .save import cmd as cmd_save
from .load import cmd as cmd_load

from .drop_item import cmd as cmd_drop
from .take_item import cmd as cmd_take
from .examine_item import cmd as cmd_examine
from .use_item import cmd as cmd_use

from .go_west import cmd as cmd_west
from .go_east import cmd as cmd_east
from .go_north import cmd as cmd_north
from .go_south import cmd as cmd_south

from .parser import parse
