from selenium import webdriver
from selenium.webdriver.common.by import By

def test_products_page(login_in_driver):
    try:
        driver = login_in_driver

        #1. Anadir un producto al carrito
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        print("Producto 'Sauce Labs Backpack' añadido al carrito.")

        #2. Validacion del contador del carrito incremente
        cart_counter = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_counter == "1", "El contador del carrito no se incrementó correctamente."
        print("Contador del carrito validado correctamente.")

        




        
    except Exception as e:
        print(f"Error en test_products_page: {e}")
        raise
    finally:
        driver.quit()



