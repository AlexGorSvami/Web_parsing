import requests
from random import  choice

url = 'http://tvoytrener.com/user-agent'

with open('user_agent.txt') as file:
    lines = file.read().split('\n')

for line in lines:
    user_agent = {'user-agent': choice(lines)}
    response = requests.get(url=url, headers=user_agent)
    print(response.text)

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT  10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
#     Chrome/99.0.4844.84 Safari/537.36',
# }
#
# response = requests.get(url='http://tvoytrener.com/user-agent')
# print(response.text)
# print(type(response))

