import os

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))


from dotenv import load_dotenv
import os

load_dotenv()

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")


def test_encryption():
    print(LOGIN)
    print(PASSWORD)
