from selenium import webdriver
import time

def test_google_search():
    # Crear una instancia del controlador de Chrome
    driver = webdriver.Chrome()
    
    # Navegar a Google
    driver.get("https://www.google.com")
    
    # Esperar 2 segundos para que puedas ver la ventana del navegador
    time.sleep(2)
    
    # Cerrar el navegador
    driver.quit()

# Llamar a la función de prueba
test_google_search()
