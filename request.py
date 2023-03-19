import requests
import json

ret = requests.get(f'https://dt.miet.ru/ppo_it_final', headers={'X-Auth-Token' : 'htbpme25'})

data = json.loads(ret.text)

for i, message in enumerate(data['message']):
    for j, point in enumerate(message['points']):
        sh = point['SH']
        distance = point['distance']
        print(f"SH={sh}, distance={distance}")
