import time # Подключение модуля для работы со временем
from selenium import webdriver # Подключение webdriver для управления браузером
import os # Модуль для работы с операционной системой

# Инициализируется драйвер браузера. Открывается новое окно брузера:
driver=webdriver.Chrome()
time.sleep(2) # Пауза 2 секунды

# Переход по ссылке:
driver.get("http://suninjuly.github.io/file_input.html") 
#time.sleep(5)

# Ищем строку, в которую нужно вписать свое имя:
name=driver.find_element_by_name("firstname")
# Пишем в строку свое имя:
name.send_keys("Elizabeth")

# Ищем строку, в которую нужно вписать свою фамилию:
lastname=driver.find_element_by_name("lastname")
# Пишем в строку свлю фамилию:
lastname.send_keys("Medvedeva")

# Ищем строку, в которую нужно вписать свой email:
email=driver.find_element_by_name("email")
# Пишем в строку свою почту:
email.send_keys("me.liza@bk.ru")

# Находим кнопку "Выберете файл":
file = driver.find_element_by_css_selector('#file')
# Получаем путь к директории текущего исполняемого файла:
current_dir = os.path.abspath(os.path.dirname(__file__))
# Добавляем к этому пути имя файла:
file_path = os.path.join(current_dir, 'file.txt')
# Добавляем файл:
file.send_keys(file_path)

# Находим элемент кнопки "Submit":
submit_button=driver.find_element_by_css_selector(".btn")
submit_button.submit() # Нажимаем на кнопку
