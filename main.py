import sys
import json
import os
sys.path.insert(0, './server')
from server import start_server

def main():
    print(' * System Starting')
    #  TODO: Carregar as consfiguracoes
    # TODO: Carregar Server HTTP
    start_server()

main()