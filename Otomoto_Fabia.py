from selenium import webdriver
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome("D:\Testy selenium\Chromedriver\chromedriver.exe")
items = []
for page in range(1,28):
    URL = "https://www.otomoto.pl/osobowe/skoda/fabia/od-2017/?search%5Border%5D=created_at%3Adesc&page=" + str(page)
    driver.get(URL)
    for item in driver.find_elements_by_class_name('offer-item'):
                params = []
                for param in item.find_elements_by_class_name('ds-param'):
                    params.append(param.find_element_by_xpath('span').text)
                params.append(item.find_element_by_class_name('offer-price__number').text)
                params.append(item.find_element_by_class_name('ds-location-region').text)
                items.append(params)

file = open('fabia_ceny_log.txt','w')
for x in items:
    print(str(x).strip('[]'))
    file.write(str(x).strip('[]')+'\n')
print('-' * 20)
file.close()




