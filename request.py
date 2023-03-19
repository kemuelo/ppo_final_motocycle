import requests
import json

ret = requests.get(f'https://dt.miet.ru/ppo_it_final', headers={'X-Auth-Token' : 'htbpme25'})

data = json.loads(ret.text)

sh_1 = data['message'][0]['points'][0]['SH']
distance_1 = data['message'][0]['points'][0]['distance']

sh_2_1 = data['message'][1]['points'][0]['SH']
distance_2_1 = data['message'][1]['points'][0]['distance']
sh_2_2 = data['message'][1]['points'][1]['SH']
distance_2_2 = data['message'][1]['points'][1]['distance']
sh_2_3 = data['message'][1]['points'][2]['SH']
distance_2_3 = data['message'][1]['points'][2]['distance']

sh_3_1 = data['message'][2]['points'][0]['SH']
distance_3_1 = data['message'][2]['points'][0]['distance']
sh_3_2 = data['message'][2]['points'][1]['SH']
distance_3_2 = data['message'][2]['points'][1]['distance']

print(sh_1, distance_1)
print(sh_2_1,distance_2_1, sh_2_2, distance_2_2, sh_2_3, distance_2_3)
print(sh_3_1,distance_3_1,sh_3_2,distance_3_2)