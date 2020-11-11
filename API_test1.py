print("#Тестирование API")


from requests import Request, Session
import json
from datetime import datetime 

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' #песочница

parameters = {
  'start':'1',
  'limit':'10',
  'convert':'USD',
  'sort_dir':"desc"
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c', #ключ для песочницы
 
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  json_data = json.loads(response.text)
  print("Запрос на url:",response.url)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

print("Код ответа:", response.status_code)
assert response.status_code == 200

print("Время ответа :", response.elapsed.total_seconds()*1000, "мс")
assert response.elapsed.total_seconds()*1000 <= 500, response.elapsed.total_seconds()*1000

print("Размер пакета данных:", len(response.content),"байт")
assert len(response.content) < 10*1024


for each in json_data['data']:
    print("Наименование валюты:", each['name'])
    print("дата последнего обновления:", each['last_updated'].split("T")[0])



today =  datetime.strftime(datetime.now(), "%Y-%m-%d")
print("Текущая дата:",today)
#assert today == each['last_updated'].split("T")[0], each['last_updated'].split("T")[0]

print("данные по запросу записаны в файл:file_response.text ")
file_data = open('file_response.text', 'wb')
file_data.write(response.content)
file_data.close()


print("Успешно")
