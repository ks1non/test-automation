import os
import json

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(ROOT_PATH, "files", "index_creds.json")

with open(path, 'r') as f:
    index_creds = json.load(f)

login = index_creds['login']
password = index_creds['password']
exception = index_creds['expectetion']
