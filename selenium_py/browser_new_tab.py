#!python3
# -*- coding: utf8 -*-

# https://stepik.org/lesson/184253/step/6?unit=158843

import math
from selenium import webdriver

browser = webdriver.Chrome()

try:

    #     1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    #     2. Нажать на кнопку
    btn = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
    btn.click()
    #     3. Переключиться на новую вкладку
    # first_window = browser.window_handles[0]
    new_window = browser.window_handles[-1]
    browser.switch_to.window(new_window)
    #     4. Пройти капчу для робота и получить число-ответ
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

# 2019-07-24T10:18:00Z
# 28.91375875251414
# Хорошие новости, верно!
# Решило: 466 Успешных решений: 89% Вы получили: 2 балла из 2
