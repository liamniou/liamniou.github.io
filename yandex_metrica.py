import requests
from urllib.parse import urlencode

app_id = 'c2ce69d0873743169b9a14ca7ef6e64a'
auth_url = 'https://oauth.yandex.com/authorize'

header = {
    'response_type': 'token',
    'client_id': app_id
}

#print('?'.join((auth_url, urlencode(header))))
token = 'AQAAAAAFZhbeAATKUX1yW0cqF03nqG0Az4pWRrQ'
#class YandexMetricaCounter: