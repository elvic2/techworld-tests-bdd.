# 🛍️ TechWorld - Pruebas Automatizadas con BDD en Behave  

## 📌 Descripción  
Este proyecto implementa pruebas automatizadas para la plataforma **TechWorld** siguiendo el enfoque **BDD (Behavior-Driven Development)**.  

A diferencia del enfoque ATDD, aquí nos centramos en definir el **comportamiento esperado del usuario** en la plataforma, asegurando que las pruebas sean colaborativas y entendibles para todo el equipo (QA, desarrollo y negocio).  

## 🚀 Tecnologías Utilizadas  
### 🔹 Lenguajes y Frameworks  
- ✅ **Python 3.x** - Lenguaje de programación principal.  
- ✅ **Behave** - Framework de **BDD (Behavior-Driven Development)** basado en Gherkin.  
- ✅ **Gherkin** - Lenguaje estructurado para definir escenarios de prueba.  
- ✅ **JSON** - Simulación de base de datos para pruebas.  

### 🔹 Herramientas de Desarrollo  
- ✅ **Git y GitHub** - Control de versiones y almacenamiento de código.  
- ✅ **Virtualenv** - Entorno virtual para aislar dependencias.  
- ✅ **VS Code** - Editores de texto.  

📌 **Repositorio del Proyecto:** https://github.com/elvic2/techworld-tests-bdd..git

---

## 📂 **Estructura del Proyecto**
techworld-tests-bdd/
│── features/                      # Archivos .feature con los escenarios de prueba BDD
│   │── authentication.feature      # Pruebas de autenticación de usuarios
│   │── orders_tracking.feature     # Pruebas de seguimiento de pedidos
│   │── cart_management.feature     # Pruebas de carrito y wishlist
│   │── product_management.feature  # Pruebas de gestión de productos
│
│── steps/                          # Implementación de los steps en Python (BDD)
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
git clone https://github.com/elvic2/techworld-tests-bdd.git
cd techworld-tests-bdd

2️⃣ Crear y Activar el Entorno Virtual
python3 -m venv venv
source venv/bin/activate   # En macOS/Linux
venv\Scripts\activate      # En Windows

3️⃣ Instalar Dependencias
pip install -r requirements.txt

✅ Ejecución de las Pruebas
#Ejecutar todas las pruebas con enfoque BDD:
behave --verbose

#Ejecutar una prueba específica:
behave features/authentication.feature
behave features/orders_tracking.feature
behave features/cart_management.feature
behave features/product_management.feature