from utils.colors import *
import os


login_pass = colors.color['White'] + '''      ╔═╗╔═╗╔═╗╔═╗╦ ╦╔═╗╦═╗╔╦╗
      ╠═╝╠═╣╚═╗╚═╗║║║║ ║╠╦╝ ║║
      ╩  ╩ ╩╚═╝╚═╝╚╩╝╚═╝╩╚══╩╝'''




menu = colors.color['White'] + 'Type help to see all commands'




search_menu = colors.color['White'] + '''                 ╔══════════════════════════════╗     ╔══════════════════════════════╗
                 ║              1               ║     ║              2               ║
                 ╠══════════════════════════════╣     ╠══════════════════════════════╣
                 ║      Search by username      ║     ║      Search by platform      ║
                 ╚══════════════════════════════╝     ╚══════════════════════════════╝'''

search_username = colors.color['White'] + '''╦ ╦╔═╗╔═╗╦═╗╔╗╔╔═╗╔╦╗╔═╗
║ ║╚═╗║╣ ╠╦╝║║║╠═╣║║║║╣ 
╚═╝╚═╝╚═╝╩╚═╝╚╝╩ ╩╩ ╩╚═╝'''

search_platform = colors.color['White'] + '''╔═╗╦  ╔═╗╔╦╗╔═╗╔═╗╦═╗╔╦╗
╠═╝║  ╠═╣ ║ ╠╣ ║ ║╠╦╝║║║
╩  ╩═╝╩ ╩ ╩ ╚  ╚═╝╩╚═╩ ╩'''




save_platform = colors.color['White'] + '''╔═╗╦  ╔═╗╔╦╗╔═╗╔═╗╦═╗╔╦╗
╠═╝║  ╠═╣ ║ ╠╣ ║ ║╠╦╝║║║
╩  ╩═╝╩ ╩ ╩ ╚  ╚═╝╩╚═╩ ╩'''

save_username = colors.color['White'] + '''╦ ╦╔═╗╔═╗╦═╗╔╗╔╔═╗╔╦╗╔═╗
║ ║╚═╗║╣ ╠╦╝║║║╠═╣║║║║╣ 
╚═╝╚═╝╚═╝╩╚═╝╚╝╩ ╩╩ ╩╚═╝'''

save_pass = colors.color['White'] + '''      ╔═╗╔═╗╔═╗╔═╗╦ ╦╔═╗╦═╗╔╦╗
      ╠═╝╠═╣╚═╗╚═╗║║║║ ║╠╦╝ ║║
      ╩  ╩ ╩╚═╝╚═╝╚╩╝╚═╝╩╚══╩╝'''

cli_input = colors.color['White'] + '> '
cli_input2 = colors.color['White'] + 'Accounts' + colors.color['Cyan'] + '@' + colors.color['White'] + os.getenv('username') + ': '

cli_choice = ' ' + colors.color['Yellow'] +'(' + colors.color['Green'] +'Y' + colors.color['White'] + '/' + colors.color['Red'] + 'n' + colors.color['Yellow'] + ')' + colors.color['White'] + ': '


main_menu = colors.color['White'] + '''                 ╔══════════════════════════════╗     ╔══════════════════════════════╗
                 ║              1               ║     ║              2               ║
                 ╠══════════════════════════════╣     ╠══════════════════════════════╣
                 ║      Search by username      ║     ║      Search by platform      ║
                 ╚══════════════════════════════╝     ╚══════════════════════════════╝'''


help_menu = colors.color['White'] + '''                      ''' + colors.color['Cyan'] + '''╔════════════════════════════════════''' + colors.color['Cyan'] + '''╗
                      ''' + colors.color['Cyan'] + '''║''' + colors.color['White'] + '''  search  ->  Search for an account ''' + colors.color['Cyan'] + '''║
                      ''' + colors.color['Cyan'] + '''║''' + colors.color['White'] + '''  save    ->  Save an account       ''' + colors.color['Cyan'] + '''║
                      ''' + colors.color['Cyan'] + '''║''' + colors.color['White'] + '''  delete  ->  Delete an account     ''' + colors.color['Cyan'] + '''║
                      ''' + colors.color['Cyan'] + '''║''' + colors.color['White'] + '''  cls     ->  Clear terminal        ''' + colors.color['Cyan'] + '''║
                      ''' + colors.color['Cyan'] + '''║''' + colors.color['White'] + '''  exit    ->  Exit program          ''' + colors.color['Cyan'] + '''║
                      ''' + colors.color['Cyan'] + '''╚════════════════════════════════════''' + colors.color['Cyan'] + '''╝'''