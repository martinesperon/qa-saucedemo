# QA Automation Project – SauceDemo Login

Este es un proyecto de automatización de pruebas con Python, Selenium y PyTest.

## ¿Qué se prueba?

1. Login con distintos usuarios (positivos y negativos).
2. Agregado de productos al carrito desde la página de inventario.
3. Verificación del contenido del carrito:
   - Validación de nombres de productos.
   - Validación de cantidad de ítems agregados.

## Tecnologías usadas:

- Python
- Selenium
- Prueba de PyTest
- Pruebas basadas en datos con archivos CSV

## Estructura de archivos:

- `data/users.csv`: usuarios de prueba
- `pages/login_page.py`: lógica del Page Object Model (POM) para login
- `pages/inventory_page.py`: lógica para agregar productos al carrito
- `pages/cart_page.py`: lógica para validar el carrito
- `tests/test_login.py`: casos de prueba de login
- `tests/test_cart.py`: casos de prueba de carrito
- `conftest.py`: configuración general (browser setup)

## Capturas automáticas:

- Si alguna prueba falla, el test guarda automáticamente una captura de pantalla en la carpeta /screenshots, con el nombre del usuario y la fecha/hora.

## Reporte HTML (report.html)
- Resultado de cada test
- Tiempo de ejecución
- Capturas de pantalla (en fallos)
- Logs y asserts

## Estado del proyecto:
- Tests parametrizados con CSV
- Page Object Model implementado
- Capturas en fallos
- Reporte HTML

## Posibles mejoras:
- Automatización CI/CD (GitHub Actions)
- Generación de datos aleatorios

## Sobre mí
Desarrollador en formación con orientación QA, buscando primeros desafíos profesionales.
Contacto:
martin.esperon133@gmail.com
