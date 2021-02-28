import json
import os

import requests
from dotenv import load_dotenv

env_path = 'environments/local.env'
load_dotenv(dotenv_path=env_path)

amounts = 80000
url = f"https://toloka.yandex.ru/api/new/requester/workers/grid?page=0&size={amounts}&ban=NOT_BANNED"

with open(os.environ['PARSER_CONFIG_PATH'], 'r') as fd:
    headers = json.load(fd)

response = requests.request("GET", url, headers=headers)

with open(os.environ['PARSER_FILE_PATH'], 'w') as fd:
    json.dump(response.json(), fd)

