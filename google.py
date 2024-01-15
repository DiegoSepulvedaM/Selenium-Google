from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Rutas a los ejecutables de Chrome y Chromedriver
chrome_binary_path = "/usr/bin/google-chrome"
chromedriver_path = "/usr/bin/chromedriver"

# Configuración de opciones de Chrome
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path

# Configuración del servicio de Chromedriver
chrome_service = ChromeService(executable_path=chromedriver_path)

# Configuración del WebDriver de Selenium
driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

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
