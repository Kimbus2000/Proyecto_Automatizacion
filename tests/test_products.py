from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_products_page(login_in_driver):
    try:
        driver = login_in_driver

        #1. Anadir un producto al carrito
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        print("Producto 'Sauce Labs Backpack' añadido al carrito.")

        time.sleep(2)
        
        #2. Validacion del contador del carrito incremente
        cart_counter = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_counter == "1", "El contador del carrito no se incrementó correctamente."
        print("Contador del carrito validado correctamente.")

        #3. Navegar al carrito de compras
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        print("Navegacion al carrito de compras validada.")
        assert "https://www.saucedemo.com/cart.html" in driver.current_url, "No se redireccionó correctamente al carrito de compras."
        
        time.sleep(3)


        
    except Exception as e:
        print(f"Error en test_products_page: {e}")
        raise
    finally:
        driver.quit()



