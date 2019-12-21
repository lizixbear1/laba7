import time # Подключение модуля для работы со временем
from selenium import webdriver # Подключение webdriver для управления браузером
import math # Подключение модуля для работы с числами

# Инициализируется драйвер браузера. Открывается новое окно брузера:
driver=webdriver.Chrome()
time.sleep(2) # Пауза 2 секунды

# Переход по ссылке:
driver.get("http://suninjuly.github.io/selects1.html") 
time.sleep(2)

def calc(x,y):
  return str((int(x)+int(y)))

# Определили значения x и y через id:
x = driver.find_element_by_id("num1").text
y = driver.find_element_by_id("num2").text

f = calc(x,y) # Нашли y через формулу выше

# Находим элемент и нажимаем на него, чтобы открылся список:
driver.find_element_by_tag_name("select").click()

# Нажимаем на вариант ответа, который соответствует значению суммы чисел:
driver.find_element_by_css_selector("[value='" + f + "']" ).click()

# Находим элемент кнопки "Submit":
submit_button=driver.find_element_by_css_selector(".btn")
submit_button.click() # Нажимаем на кнопку
