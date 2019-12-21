from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time # Подключение модуля для работы со временем
from selenium import webdriver # Подключение webdriver для управления браузером
import math

# Инициализируется драйвер браузера. Открывается новое окно брузера:
driver=webdriver.Chrome()
time.sleep(2) # Пауза 2 секунды

driver.implicitly_wait(5)
# Переход по ссылке:
driver.get("http://suninjuly.github.io/explicit_wait2.html") 
time.sleep(2)

button = WebDriverWait(driver, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

butt = driver.find_element_by_id('book')
butt.click()

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
submit_button=driver.find_element_by_id("solve")
submit_button.submit() # Нажимаем на кнопку

