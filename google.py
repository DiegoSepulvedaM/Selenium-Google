from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time

# Establece la ruta de chromedriver
driver = webdriver.Chrome('/usr/bin/chromedriver')

# Configura el servicio de Chrome con la ruta al chromedriver
chrome_service = webdriver.ChromeService(executable_path=driver)

# Configura el webdriver utilizando el servicio de Chrome
driver = webdriver.Chrome(service=chrome_service)

try:
    # Realiza la búsqueda en Google
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Jenkins")
    search_box.send_keys(Keys.RETURN)

    # Espera un momento para ver los resultados
    time.sleep(2)

    # Captura un screenshot para verificar el resultado (opcional)
    driver.save_screenshot("google_search_results.png")
finally:
    # Cierra el navegador al finalizar
    driver.quit()


