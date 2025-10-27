# Proyecto de Automatización de Pruebas (Saucedemo)

Este proyecto contiene un conjunto de pruebas automatizadas (End-to-End) para el sitio web de e-commerce [Saucedemo.com](https://www.saucedemo.com/).

## 1. Propósito del Proyecto

El objetivo principal es validar el flujo de usuario completo (E2E) en la plataforma, asegurando que las funcionalidades críticas operen correctamente. Las pruebas cubren:

* **Login:** Verificación de inicio de sesión exitoso.
* **Catálogo (Inventario):** Verificación de la visualización de productos, título de la página y elementos de la interfaz (menú, filtros).
* **Carrito de Compras:** Simulación del proceso de añadir un producto y verificar que este se refleje correctamente en el carrito.

---

## 2. Tecnologías Utilizadas

* **Lenguaje:** Python
* **Automatización de Navegador:** Selenium WebDriver
* **Framework de Pruebas:** Pytest
* **Reportes:** pytest-html (para la generación de reportes visuales)

---

## 3. Instalación de Dependencias

Para ejecutar este proyecto, necesitas tener instalado Python 3.10+ y Google Chrome.

**1. Prerrequisitos:**

* **Google Chrome:** Asegúrate de tener el navegador instalado.
* **ChromeDriver:** Descarga el [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) que corresponda **exactamente** a tu versión de Google Chrome. Debes colocar el archivo `chromedriver.exe` en una carpeta que esté incluida en el PATH de tu sistema.

**2. Entorno Virtual (Recomendado):**

Se recomienda crear un entorno virtual para aislar las dependencias del proyecto.

```bash
# Crear el entorno
python -m venv venv

# Activar en Windows
.\venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate