import requests
# from urllib.parse import urlencode

# app_id = 'c2ce69d0873743169b9a14ca7ef6e64a'
# auth_url = 'https://oauth.yandex.com/authorize'
#
# header = {
#     'response_type': 'token',
#     'client_id': app_id
# }

# print('?'.join((auth_url, urlencode(header))))

class YandexMetricaStats:
    def __init__(self, token, counter_name):
        self.token = token
        self.counter_name = counter_name

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/json'
        }

    def get_counter_id(self):
        headers = self.get_headers()
        response = requests.get('https://api-metrika.yandex.ru/management/v1/counters?search_string={0}'.format(self.counter_name),
                                headers=headers, params={'pretty': 1})
        return response.json()['counters'][0]['id']

    def get_data(self, metrics):
        headers = self.get_headers()
        counter_id = self.get_counter_id()
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data?id={0}&metrics={1}'.format(counter_id, metrics),
                                headers=headers, params={'pretty': 1})
        return int(response.json()['totals'][0])

    def get_visits(self):
        return 'Суммарное количество визитов: {0}'.format(self.get_data('ym:s:visits'))

    def get_page_views(self):
        return 'Суммарное количество просмотров: {0}'.format(self.get_data('ym:pv:pageviews'))

    def get_users(self):
        return 'Суммарное количество посетителей: {0}'.format(self.get_data('ym:pv:users'))

token = 'AQAAAAAFZhbeAATKUX1yW0cqF03nqG0Az4pWRrQ'
counter_name = 'liamnou.github.io'

current_session = YandexMetricaStats(token, counter_name)
print(current_session.get_counter_id())
visits = current_session.get_visits()
print(visits)
page_views = current_session.get_page_views()
print(page_views)
users = current_session.get_users()
print(users)