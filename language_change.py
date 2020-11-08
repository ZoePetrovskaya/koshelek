#1. подключение webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.select import Select  
import time 



#2. открытие ресурса
driver = webdriver.Chrome() 
driver.maximize_window()
driver.get("http://coinmarketcap.com")
driver.implicitly_wait(20)


#3. автоматизированные тесты для переключения языков coinmarketcap.com.

print("#1. Кейс 1 Проверка смены языка на вьетнамский язык")
language_sort = driver.find_element_by_class_name("sc-10o4ja6-0.iwazsF").click()
input_language = driver.find_element_by_class_name("sc-1jme59x-1.dPwqZh.cmc-input").send_keys("Tiếng Việt")
lang = driver.find_elements(By.CLASS_NAME, "cmc-language-picker__option")
lang[0].click()
time.sleep(20)
current_page = driver.current_url
print(current_page)
assert current_page =="https://coinmarketcap.com/vi/"

print("#2. Кейс 2 Проверка смены языка на последний в списке")
language_sort = driver.find_element_by_class_name("sc-10o4ja6-0.iwazsF").click()
lang = driver.find_elements(By.CLASS_NAME, "cmc-language-picker__option")
lang[-1].click()
time.sleep(20)
current_page = driver.current_url
print(current_page)
assert current_page =="https://coinmarketcap.com/zh-tw/"

print("#3. Кейс 3 Получение списка языков")
language_sort = driver.find_element_by_class_name("sc-10o4ja6-0.iwazsF").click()
lang = driver.find_elements(By.CLASS_NAME, "cmc-language-picker__option")
lang_text =[]
for x in lang:
    lang_text.append(x.text)
print(lang_text)
if len(lang)==32:
    print("Возможен выбор из 32 языков")
else:
    print(len(lang))

print("#4. Кейс  Поиск по первым буквам")

driver.get("http://coinmarketcap.com")
language_sort = driver.find_element_by_class_name("sc-10o4ja6-0.iwazsF").click()

input_language = driver.find_element_by_class_name("sc-1jme59x-1.dPwqZh.cmc-input").send_keys("it")
lang = driver.find_elements(By.CLASS_NAME, "cmc-language-picker__option")
print(len(lang))
lang[0].click()

current_page = driver.current_url
print(current_page)
assert current_page =="https://coinmarketcap.com/it/"

print("#5. Кейс  Ввод некорректных символов")
driver.get("http://coinmarketcap.com")
current_page_before = driver.current_url
language_sort = driver.find_element_by_class_name("sc-10o4ja6-0.iwazsF").click()

input_language = driver.find_element_by_class_name("sc-1jme59x-1.dPwqZh.cmc-input").send_keys("#@%")
lang = driver.find_elements(By.CLASS_NAME, "cmc-language-picker__option")
print(len(lang))

print("Успешно")
driver.quit()