from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')  # Esta opción solo es aplicable para sistemas operativos Windows
chrome_options.binary_location = '/usr/bin/google-chrome'  # Ajusta la ruta según tu entorno

chromedriver_path = '/usr/bin/chromedriver'  # Ajusta la ruta según tu entorno
driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver_path)

try:
    # Acciones del script aquí...
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Jenkins")
    search_box.send_keys(Keys.RETURN)

    # Esperar un momento para ver los resultados
    time.sleep(2)

    # Puedes agregar más acciones aquí...

finally:
    # Cerrar el navegador al finalizar
    driver.quit()
