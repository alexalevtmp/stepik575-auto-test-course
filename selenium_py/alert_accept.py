#!python3
# -*- coding: utf8 -*-

# https://stepik.org/lesson/184253/step/4?unit=158843

import math
from selenium import webdriver

browser = webdriver.Chrome()

try:
    
    #     1. Открыть страницу http://suninjuly.github.io/alert_accept.html
    link = "https://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    #     2. Нажать на кнопку
    btn = browser.find_element_by_tag_name("button")
    btn.click()
    #     3. Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()
    #     4. На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = browser.find_element_by_id("input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:

    browser.close()
    browser.quit()

# 2019-07-24T08:14:00Z
# 28.912886377088306
# Верно.
# Решило: 475 Успешных решений: 95% Вы получили: 2 балла из 2
