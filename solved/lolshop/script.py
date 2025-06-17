#! /usr/bin/python3
import gzip
import base64


state = bytes(input(),'ascii')
print(state)
state = gzip.compress(state)
print(state)
state = base64.b64encode(state)
print(str(state))
#data = {}
#data['state'] = state
#response = requests.post('http://lolshop.training.jinblack.it/api/add_to_cart.php', data)
#print(response.status_code)
#print(response.content)
