from selenium import webdriver
from selenium.webdriver.common.by import By

def test_inventory_page(login_in_driver):
    try:
        driver = login_in_driver

        # 1. Criterio mínimo: Verificamos el título de la página de inventario
        assert driver.title == "Swag Labs", "El título de la página no es correcto."
        print("Título de la página validado correctamente.")

        # 2. Criterio mínimo: Verificamos que haya productos listados en la página de inventario
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No se encontraron productos en la página de inventario."
        print("Página de inventario validada correctamente.")

        # 3. Criterio mínimo: Listar nombre/precio del primer producto
        first_product = products[0]
        product_name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
        product_price = first_product.find_element(By.CLASS_NAME, "inventory_item_price").text
        assert product_name and product_price, "El nombre o precio del primer producto están vacíos."
        print(f"Primer producto: {product_name}, Precio: {product_price}")

        #4. Validación de elementos de la interfaz (Menú y Filtros)

        # Verificar que el menú esté visible
        menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu_button.is_displayed(), "El menú no está visible."
        print("Menú validado correctamente.")

        # Verificar que el filtro esté visible
        filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filter_dropdown.is_displayed(), "El filtro no está visible."
        print("Filtro validado correctamente.")

        # Validar que el carrito de compras esté visible
        cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        assert cart_button.is_displayed(), "El carrito de compras no está visible."
        print("Carrito de compras validado correctamente.")

    except Exception as e:
        print(f"Error en test_inventory_page: {e}")
        raise
    finally:
        driver.quit()