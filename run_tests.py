import pytest

#Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_inventory.py",
    "tests/test_login.py",
    "tests/test_products.py",
    # Agrega aquí otros archivos de prueba según sea necesario
]

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report.html", "--self-contained-html","-v"]

pytest.main(pytest_args)