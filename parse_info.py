import json
import os

import requests
from dotenv import load_dotenv


def get_workers(w_id, requester_id):
    worker = {}
    url = f'https://toloka.yandex.ru/api/new/requester/workers/{w_id}'
    response = requests.get(url, headers=headers)
    worker['info'] = response.json()
    url = f'https://toloka.yandex.ru/api/new/requester/workers/{w_id}/attributes?page=0&size=100'
    response = requests.get(url, headers=headers)
    worker['attributes'] = response.json()
    url = f'https://toloka.yandex.ru/api/new/requester/workers/{w_id}/skills?page=0&size=500&requesterIds={requester_id}&scope=REQUESTER_LIST&permission=USER_SKILL__READ'
    response = requests.get(url, headers=headers)
    worker['skills'] = response.json()
    url = f'https://toloka.yandex.ru/api/new/requester/workers/{w_id}/skills?page=0&size=500&requesterIds={requester_id}&scope=REQUESTER_LIST&permission=USER_SKILL__READ'
    response = requests.get(url, headers=headers)
    worker['skills'] = response.json()
    url = f'https://toloka.yandex.ru/api/new/requester/workers/{w_id}/income-log?page=0&size=10&from=2010-01-18&to=2030-01-19'
    response = requests.get(url, headers=headers)
    worker['income'] = response.json()
    return worker


env_path = 'environments/local.env'
load_dotenv(dotenv_path=env_path)

with open(os.environ['PARSER_FILE_PATH'], 'r') as fd:
    data = json.load(fd)
with open(os.environ['PARSER_CONFIG_PATH'], 'r') as fd:
    headers = json.load(fd)
requester_id_ = os.environ['PARSER_REQUESTER_ID']
output_dir = os.environ['PARSER_OUTPUT_DIR']

for item in data['content']:
    fname = f'{output_dir}{item["workerId"]}.json'
    if os.path.isfile(fname):
        continue
    with open(fname, 'w') as fd:
        d = get_workers(item['workerId'], requester_id_)
        json.dump(d, fd)
