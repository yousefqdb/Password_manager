from functions.json import *
from utils.file import *
from utils.colors import *
from config.designs import *
from functions.get_ttl_lines import get_ttl_lines
from functions.encryption import *

class acc:
    def search():

        colors.cls()
        print(search_menu)
        opt = input(cli_input)

        if opt == '1':
            colors.cls()
            print(search_username)
            word = input(cli_input)

        elif opt == '2':
            colors.cls()
            print(search_platform)
            word = input(cli_input)
            
        db__ = get_db_location()
        colors.cls()
        with open(db__) as db:
            lines = db.readlines()
            for row in lines:
                if row.find(word) != -1:
                    output_ = row.split()
                    print(colors.color['Cyan'] + output_[0] + colors.color['White'] +  ' ' + output_[1] + ' ********')
                else:
                    print(colors.color['Red'] + 'No results' + colors.color['Red'])
                    return

            print('\n\n')
            choice = input('Show password' + colors.color['Yellow'] + '(' + colors.color['Cyan'] + 's' + colors.color['Yellow'] + ')?' + cli_choice)
            if choice == 'y' or choice == 'Y' or choice == '':
                colors.cls()
                for row in lines:
                    if row.find(word) != -1:
                        output_ = row.split()
                        dec_pass = crypt.decrypt(output_[2])
                        print(colors.color['Cyan'] + output_[0] + colors.color['White'] +  ' ' + output_[1] + ' ' + dec_pass)
            print('\n')




    def save():
        colors.cls()
        print(save_platform)
        platform = input(cli_input)

        colors.cls()
        print(save_username)
        username = input(cli_input)

        colors.cls()
        print(save_pass)
        password = input(cli_input)

        colors.cls()

        print(colors.color['Cyan'] + 'Platform' + colors.color['White'] + ': ' + platform)
        print(colors.color['Cyan'] + 'Username' + colors.color['White'] + ': ' + username)
        print(colors.color['Cyan'] + 'Password' + colors.color['White'] + ': ' + password + '\r\n')

        choice = input('Do you want to continue?' + cli_choice)

        if choice == 'y' or choice == 'Y' or choice == '':
            db = get_db_location()
            enc_pass = crypt.encrypt(password)
            file.write(db, platform + ' ' + username + ' ' + enc_pass + ' ')
            print(colors.color['Green'] +' Account saved' + colors.color['Green'] + '!')




    def delete():
        colors.cls()
        print(search_platform)
        platform = input(cli_input)

        colors.cls()
        print(search_username)
        username = input(cli_input)


        line_num = 0

        db__ = get_db_location()
        lines = get_ttl_lines(db__)


        colors.cls()

        with open(db__) as db:
            lines = db.readlines()
            for row in lines:
                if row.find(platform) != -1:
                    if row.find(username) != -1:
                        output_ = row.split()
                        dec_pass = crypt.decrypt(output_[2])
                        print(colors.color['Cyan'] + output_[0] + colors.color['White'] +  ' ' + output_[1] + ' ' + dec_pass)
                        choice = input('Are you sure you want to delete this account?' + cli_choice)
                        if choice == 'y' or choice == 'Y' or choice == '':
                            line_num = lines.index(row)
                            with open(db__, 'w') as db:
                                for number, line in enumerate(lines):
                                    if number not in [line_num]:
                                        db.write(line)
                                        print(colors.color['Green'] + 'Account deleted successfully' + colors.color['White'] + '!')
                        else:
                            print(colors.color['Red'] + 'Account deletion cancled' + colors.color['White'] + '!')