import requests
import json

ret = requests.get(f'https://dt.miet.ru/ppo_it_final', headers={'X-Auth-Token' : 'rr6jtsww'})

print(f'Status code: {ret.status_code}\nText     : {ret.text}')