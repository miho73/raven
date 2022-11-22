import sys

import builder
import transform

USAGE ='''Usage: raven <command>'''

## Read arugments
if len(sys.argv) == 1:
    print(USAGE)
    exit(-1)

command = sys.argv[1]

if command == 'build':
    builder.build()
    print('build completed')
elif command == 'export':
    transform.export()
elif command == 'import':
    if(len(sys.argv) <= 2):
        print('''Usage: raven import <Path>''')
    else:
        transform.imp(sys.argv[2])
else:
    print('Unknown command', command,'\n',USAGE)
