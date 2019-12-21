import time # Подключение модуля для работы со временем
import math # Подключение модуля для работы с числами
from selenium import webdriver # Подключение webdriver для управления браузером

# Инициализируется драйвер браузера. Открывается новое окно брузера:
driver=webdriver.Chrome()
time.sleep(2) # Пауза 2 секунды

# Переход по ссылке:
driver.get("http://suninjuly.github.io/execute_script.html") 
#time.sleep(2)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Взяли значение, которое является значением х для задачи:
x_element = driver.find_element_by_id("input_value").text
x = x_element
y = calc(x) # Нашли y через формулу выше

# Проскролить страницу вниз:
button = driver.find_element_by_tag_name("button")
driver.execute_script("window.scrollBy(0,110);")

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
