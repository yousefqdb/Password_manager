from utils.colors import *
from procs.accounts import *
from utils.file import *
from config.designs import *
from functions.json import *

def handler():
    while True:
        cmd = input(cli_input2)

        if cmd == 'search':
            acc.search()

        elif cmd == 'save':
            acc.save()

        elif cmd == 'delete':
            acc.delete()

        elif cmd == 'help':
            colors.cls()
            print(help_menu)

        elif cmd == 'cls':
            colors.cls()

        elif cmd == 'exit':
            exit()