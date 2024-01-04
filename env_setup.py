import os
import json
# для доступа к данным в папке files
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
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

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")


def test_encryption():  # try printing your secrets while running the code in CI to check if they are really encrypted
    print(LOGIN)
    print(PASSWORD)
