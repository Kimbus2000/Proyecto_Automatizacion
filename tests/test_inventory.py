from selenium import webdriver
from selenium.webdriver.common.by import By

def test_inventory_page(login_in_driver):
    try:
        driver = login_in_driver

        # Verificamos el título de la página de inventario
        assert driver.title == "Swag Labs", "El título de la página no es correcto."
        print("Título de la página validado correctamente.")

        # Verificamos que haya productos listados en la página de inventario
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No se encontraron productos en la página de inventario."
        print("Página de inventario validada correctamente.")

        

    except Exception as e:
        print(f"Error en test_inventory_page: {e}")
        raise
    finally:
        driver.quit()