from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_google_search():
    chromedriver_path = "/usr/bin/chromedriver"  # Reemplaza con la ubicación correcta de chromedriver
    chrome_binary_path = "/usr/bin/google-chrome"  # Reemplaza con la ubicación correcta de Google Chrome

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_binary_path

    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

    try:
        driver.get("https://www.google.com")
        search_box = driver.find_element("name", "q")
        search_box.send_keys("Jenkins")
        search_box.send_keys(Keys.RETURN)

        # Espera un momento para ver los resultados
        time.sleep(2)

        # Captura un screenshot para verificar el resultado (opcional)
        driver.save_screenshot("google_search_results.png")
    finally:
        driver.quit()

# Llama a la función de prueba
test_google_search()

