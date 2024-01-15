from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Establece la ruta de chromedriver
chromedriver_path = "/usr/bin/chromedriver"
chrome_binary_path = "/usr/bin/google-chrome"

# Configura las opciones de Chrome
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--window-position=0,0")
options.add_argument("--headless")
options.add_argument("--no-sandbox")  # Agrega la opción --no-sandbox

# Configura el servicio de Chrome con la ruta al chromedriver
chrome_service = ChromeService(executable_path=chromedriver_path)

# Configura el webdriver utilizando el servicio de Chrome y las opciones
driver = webdriver.Chrome(service=chrome_service, options=options)

try:
    # Realiza la búsqueda en Google
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Diego")
    search_box.send_keys(Keys.RETURN)

    # Espera un momento para ver los resultados
    time.sleep(2)

    # Captura un screenshot para verificar el resultado (opcional)
    driver.save_screenshot("google_search_results.png")

finally:
    # Cierra el navegador al finalizar
    driver.quit()



