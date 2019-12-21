import time # Подключение модуля для работы со временем
from selenium import webdriver # Подключение webdriver для управления браузером
import math

# Инициализируется драйвер браузера. Открывается новое окно брузера:
driver=webdriver.Chrome()
time.sleep(2) # Пауза 2 секунды

# Переход по ссылке:
driver.get("http://suninjuly.github.io/alert_accept.html") 
#time.sleep(2)

# Находим кнопку:
driver.find_element_by_css_selector(".btn").click()

# Переключаемся на окно и нажимаем согласиться с сообщением:
confirm = driver.switch_to.alert
confirm.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Взяли значение, которое является значением х для задачи:
x_element = driver.find_element_by_id("input_value")
x = x_element.text
y = calc(x) # Нашли y через формулу выше

# Ищем строку, в которую нужно вписать ответ функции:
textinput=driver.find_element_by_id("answer")

# Пишем в строку ответа значение результата функции:
textinput.send_keys(y)

# Находим элемент кнопки "Submit":
submit_button=driver.find_element_by_css_selector(".btn")
submit_button.click() # Нажимаем на кнопку

