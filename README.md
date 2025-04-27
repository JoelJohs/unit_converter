# Conversor de Unidades

[![Flask](https://img.shields.io/badge/Flask-3.1.0-blue.svg)](https://flask.palletsprojects.com/) [![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-blue.svg)](https://getbootstrap.com/)

---

## Índice

- [Rutas y Funcionalidades](#rutas-y-funcionalidades)
- [Interfaz de Usuario](#interfaz-de-usuario)
- [Cómo usarla](#cómo-usarla)
- [Instalación](#instalación)
- [Repositorio](#url-del-repositorio)

---

## Rutas y Funcionalidades

- **/**: Página de inicio que utiliza la plantilla base (base.html).
- **/length**: Conversión de unidades de longitud _(milímetro, centímetro, metro, kilómetro, pulgada, pie, yarda, milla)_.
- **/weight**: Conversión de unidades de peso _(miligramo, gramo, kilogramo, onza, libra)_.
- **/temperature**: Conversión de unidades de temperatura _(celsius, fahrenheit, kelvin)_.

---

## Interfaz de Usuario

- Utiliza **Bootstrap** para un diseño limpio y responsivo.
- Emplea la plantilla **base.html** que define la barra de navegación y la estructura general.
- Los formularios permiten ingresar valores y seleccionar las unidades para la conversión.

---

## Cómo usarla

1. Instala Python 3.x y Flask (`pip install flask`).
2. Ejecuta la aplicación con `python app.py`.
3. Accede a [http://127.0.0.1:5000/](http://127.0.0.1:5000/) en tu navegador.
4. Selecciona la ruta deseada mediante la barra de navegación.
5. Ingresa los datos y recibe el resultado instantáneo de la conversión.

---

## Instalación

- Asegúrate de tener Python 3.x instalado.
- Instala las dependencias ejecutando:
  ```bash
  pip install -r requirements.txt
  ```
- Ejecuta la aplicación:
  ```bash
  python app.py
  ```

---

## URL del Repositorio

[https://github.com/JoelJohs/unit_converter](https://github.com/JoelJohs/unit_converter)
