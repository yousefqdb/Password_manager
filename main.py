from config.designs import *
from utils.colors import *
from handler.main import handler
from functions.encryption import *

print(login_pass)
pass__ = input(cli_input)
db__ = get_admin_db_location()
colors.cls()
with open(db__, 'r') as db:
    lines = db.readlines()
    for row in lines:
        dec_pass = crypt.decrypt(row)
        if pass__ != dec_pass:
            print('INVALID KEY!')
            exit()
colors.cls()
print(menu)

handler()