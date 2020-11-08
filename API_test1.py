print("#Тестирование API")


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
#url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' #песочница
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'10',
  'convert':'USD',
  'sort_dir':"desc"
}
headers = {
  'Accepts': 'application/json',
  #'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c', #ключ для песочницы
  'X-CMC_PRO_API_KEY': '05acc93f-3277-4d90-854d-7661d306874f',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  json_data = json.loads(response.text)
#  print(json_data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

print("Код ответа:", response.status_code)
assert response.status_code == 200, response.status_code
print("Время ответа :", response.elapsed.total_seconds()*1000, "мс")
assert response.elapsed.total_seconds()*1000 <= 1000, "Время ответа превышает допустимое"


for each in json_data['data']:
    print("Наименование валюты:", each['name'])
    print("дата последнего обновления:", each['last_updated'])

file_data = open('file_response.text', 'w')
file_data.write(str(json_data))
file_data.close()


print("Размер файла:", os.stat('file_response.text').st_size/1024 ,"Кб")
assert os.stat('file_response.text').st_size/1024 < 10, "Размер данных превышает допустимой значение"
print("Успешно")
