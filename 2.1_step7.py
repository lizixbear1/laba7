import time # Подключение модуля для работы со временем
from selenium import webdriver # Подключение webdriver для управления браузером
import math # Подключение модуля для работы с числами

# Инициализируется драйвер браузера. Открывается новое окно брузера:
driver=webdriver.Chrome()
time.sleep(2) # Пауза 2 секунды

# Переход по ссылке:
driver.get("http://suninjuly.github.io/get_attribute.html") 
time.sleep(2)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Нашли картинку с изображением сундука с сокровищами:
robots_radio = driver.find_element_by_id("treasure")

# Взяли значение valuex, которое является значением х для задачи:
x_element = robots_radio.get_attribute("valuex")
x = x_element
y = calc(x) # Нашли y через формулу выше

# Ищем строку, в которую нужно вписать ответ функции:
textinput=driver.find_element_by_id("answer")

# Пишем в строку ответа значение результата функции:
textinput.send_keys(y)

# Находим элемент, в котором необходимо поставить галочку:
option1 = driver.find_element_by_id("robotCheckbox")
option1.click() # Ставим галочку

# Находим элемент, в котором необходимо поставить переключатель:
option2 = driver.find_element_by_id("robotsRule")
option2.click() # Ставим переключатель

# Находим элемент кнопки "Submit":
submit_button=driver.find_element_by_css_selector(".btn")
submit_button.click() # Нажимаем на кнопку

