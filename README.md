# 🛍️ TechWorld - Pruebas Automatizadas con Behave ATDD

## 📌 Descripción
Este proyecto contiene pruebas automatizadas para la plataforma de e-commerce **TechWorld**, utilizando **Behave** y el lenguaje **Gherkin**.  

Se validan las siguientes funcionalidades principales:
- 🔐 **Autenticación de usuarios** (Registro, Inicio de sesión, Bloqueo por intentos fallidos).
- 📦 **Seguimiento de pedidos** (Consulta de estado, cambios de estado, notificaciones).
- 🛒 **Gestión del carrito y wishlist** (Agregar, modificar cantidades, stock).
- 🏪 **Gestión de productos** (Crear, modificar, activar/desactivar productos).

---

## 🚀 **Tecnologías Utilizadas**
- **Python 3.x**
- **Behave** (Framework BDD para pruebas automatizadas)
- **JSON** (Simulación de base de datos)
- **Gherkin** (Lenguaje de especificación de pruebas)
- **Virtualenv** (Entorno virtual de Python)

---

## 📂 **Estructura del Proyecto**
techworld-tests/
│── features/                      # Archivos .feature con los escenarios de prueba
│   │── authentication.feature      # Pruebas de autenticación de usuarios
│   │── orders_tracking.feature     # Pruebas de seguimiento de pedidos
│   │── cart_management.feature     # Pruebas de carrito y wishlist
│   │── product_management.feature  # Pruebas de gestión de productos
│
│── steps/                          # Implementación de los steps en Python
│   │── authentication_steps.py     # Steps de autenticación
│   │── orders_tracking_steps.py    # Steps de seguimiento de pedidos
│   │── cart_management_steps.py    # Steps de carrito y wishlist
│   │── product_management_steps.py # Steps de gestión de productos
│
│── data/                           # Simulación de base de datos en JSON
│   │── users.json                   # Usuarios registrados
│   │── orders.json                  # Pedidos
│   │── cart.json                    # Carrito de compras
│   │── wishlist.json                 # Wishlist de productos
│   │── products.json                 # Productos registrados
│
│── environment.py                   # Configuración global de Behave
│── requirements.txt                  # Dependencias del proyecto
│── behave.ini                        # Configuración adicional de Behave
│── README.md                         # Documentación del proyecto

---

## 📥 **Instalación y Configuración**
### 1️⃣ **Clonar el Repositorio**
```bash
git clone ttps://github.com/elvic2/PruebasFuncionalesVictor.git
cd techworld-tests

2️⃣ Crear y Activar el Entorno Virtual
    python3 -m venv venv
    source venv/bin/activate   # En macOS/Linux
    venv\Scripts\activate      # En Windows

3️⃣ Instalar Dependencias
    pip install -r requirements.txt

✅ Ejecución de las Pruebas
    #TODAS
    behave --verbose

    ##ESPECIFICAS
    behave features/authentication.feature
    behave features/orders_tracking.feature
    behave features/cart_management.feature
    behave features/product_management.feature

Autor: Victor Hugo Vargas Franco, Pruebas de requisitos funcioanales
📩 Email: victorh.vargasf@autonoma.edu.co
