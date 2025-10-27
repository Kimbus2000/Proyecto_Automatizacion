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

        #4. Validar que el mismo producto añadido esté en el carrito y no otro
        product_name_in_cart = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert product_name_in_cart == "Sauce Labs Backpack", f"Producto incorrecto en el carrito. Se esperaba 'Sauce Labs Backpack' pero se encontró '{product_name_in_cart}'."
        print(f"Verificación exitosa: '{product_name_in_cart}' está en el carrito.")
        time.sleep(2)
        
    except Exception as e:
        print(f"Error en test_products_page: {e}")
        raise
    finally:
        driver.quit()



