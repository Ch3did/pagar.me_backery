import sys
import json
import os
sys.path.insert(0, './server')
from server import start_server

def main():
    print(' * System Starting')
    #  TODO: Carregar as consfiguracoes


    with open('/etc/' + os.getenv('PME_BACKERY') + '/config.json') as json_file:
        data = json.load(json_file)

    # TODO: Carregar Server HTTP
    start_server()

main()