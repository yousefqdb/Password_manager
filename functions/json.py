import json
config = 'C:\\Users\\youse\\OneDrive\\Desktop\\code\\py\\Password_manager\\config\\main.json'

def get_db_location():
    with open(config, 'r') as cnfg:
        a = json.load(cnfg)
    return a["db_location"]

def get_admin_db_location():
    with open(config, 'r') as cnfg:
        a = json.load(cnfg)
    return a["admin_db_location"]

def get_enc_key():
    with open(config, 'r') as cnfg:
        a = json.load(cnfg)
    return a["enc_key"]