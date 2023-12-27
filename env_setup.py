# import os
# import json
# для доступа к данным в папке files
# ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
# path = os.path.join(ROOT_PATH, "files", "index_creds.json")
#
# with open(path, 'r') as f:
#     index_creds = json.load(f)
#
# login = index_creds['login']
# password = index_creds['password']
# exception = index_creds['expectetion']

from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_1 = os.getenv("TOKEN_1")
TOKEN_2 = os.getenv("TOKEN_2")


def test_encryption(): # try printing your secrets while running the code in CI to check if they are really encrypted
    print(TOKEN_1)
    print(TOKEN_2)