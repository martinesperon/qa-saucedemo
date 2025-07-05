# QA Automation Project – SauceDemo Login

Este es un proyecto de automatización de pruebas con Python, Selenium y PyTest.

## ¿Qué se prueba?

Se automatiza el login en [https://www.saucedemo.com](https://www.saucedemo.com) con diferentes usuarios, validando tanto accesos exitosos como fallidos.

## Tecnologías usadas:

- Python 3.x
- Selenium
- PyTest
- Data-driven testing con archivos CSV

## Estructura de archivos:

- `data/users.csv`: usuarios de prueba
- `pages/login_page.py`: lógica del Page Object Model (POM)
- `tests/test_login.py`: casos de prueba
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
- Tests para otras funcionalidades del sitio
- Generación de datos aleatorios

## Sobre mí
Desarrollador en formación con orientación QA, buscando primeros desafíos profesionales.
Contacto:
martin.esperon133@gmail.com
