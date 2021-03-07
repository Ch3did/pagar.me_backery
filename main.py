# import sys
# sys.path.insert(0, './server')
import json
import os
from server.server import start_server

def main():
    print(' * System Starting')
    # TODO: Carregar as consfiguracoes
    configs = {
        "db": {
            "user": "root",
            "password": "123456",
            "host": "localhost",
            "database": "pagarMe"
        }
    }

    # TODO: Carregar Server HTTP
    start_server(configs)

main()