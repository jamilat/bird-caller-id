import sys
import re

'''Helper code used to set-up the rest of the code:'''

class Bird:
    def __init__(self, scientific_name = 'AVES', common_name = 'BIRD', colour = 'UNKOWN'):
        self.scientific_name = scientific_name
        self.common_name = common_name
        self.colour = colour



'''Code with logic and calls to other functions:'''
if len(sys.argv) < 2:
    sys.exit('No argument input. Enter a valid audio file.')

m = re.search(f'(.*)', sys.argv[1])
if m == None:
    sys.exit('No valid file input. Enter a valid audio file.')

print(m.groups())

