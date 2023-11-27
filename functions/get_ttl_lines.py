from functions.json import *

def get_ttl_lines(db):
    lines = []
    with open(db, 'r') as fp:
        lines = fp.readlines()
    
    return lines