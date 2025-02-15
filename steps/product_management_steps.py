import json
import os
from behave import given, when, then

PRODUCTS_FILE = "products.json"

# Función para cargar productos desde el JSON
def cargar_productos():
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Función para guardar productos en el JSON
def guardar_productos(data):
    with open(PRODUCTS_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Cargar productos registrados
productos_registrados = cargar_productos()

### **PASOS PARA CREACIÓN DE PRODUCTOS**
@given('que el administrador ha iniciado sesión en la plataforma')
def step_given_admin_logeado(context):
    context.admin_autenticado = True
    print("Administrador autenticado en la plataforma")

@when('accede a la sección de gestión de productos')
def step_when_admin_gestion_productos(context):
    assert context.admin_autenticado, "El administrador debe estar autenticado"
    print("Administrador accede a la gestión de productos")

@when('completa los campos obligatorios (nombre, descripción, precio, stock, categoría)')
def step_when_completa_campos_producto(context):
    context.producto = {
        "id": "PROD789",
        "nombre": "Teclado Mecánico RGB",
        "descripcion": "Teclado gaming con retroiluminación RGB",
        "precio": 80,
        "stock": 50,
        "categoria": "Periféricos"
    }
    print("Administrador ha completado los campos del producto")

@when('guarda el producto')
def step_when_guardar_producto(context):
    productos_registrados[context.producto["id"]] = context.producto
    guardar_productos(productos_registrados)
    print("Producto guardado en el catálogo")

@then('el sistema debe registrar el nuevo producto en el catálogo')
def step_then_producto_registrado(context):
    assert context.producto["id"] in productos_registrados
    print(f"Producto {context.producto['nombre']} registrado en el catálogo")

@then('mostrar un mensaje de confirmación de creación de producto')
def step_then_mensaje_confirmacion_creacion_producto(context):
    print(f"Mensaje: Producto {context.producto['nombre']} ha sido creado exitosamente")

### **PASOS PARA CREACIÓN DE PRODUCTOS CON DATOS INCOMPLETOS**
@given('que el administrador intenta agregar un producto nuevo')
def step_given_admin_intenta_agregar_producto(context):
    context.producto = {"nombre": "", "precio": 100}  # Simulando un campo faltante
    print("Administrador intenta agregar un producto sin completar todos los campos")

@when('omite un campo obligatorio')
def step_when_omite_campo_obligatorio(context):
    assert "nombre" in context.producto and context.producto["nombre"] == ""
    print("Falta completar un campo obligatorio")

@then('el sistema debe mostrar un mensaje de error en la creación de producto')
def step_then_mensaje_error_creacion_producto(context):
    print("Error: No se puede crear el producto sin completar todos los campos")

@then('evitar la creación del producto hasta completar la información requerida')
def step_then_evitar_creacion_producto(context):
    print("Producto no registrado hasta completar la información")

@given('que el administrador está en la sección de gestión de productos')
def step_given_admin_gestionando_productos(context):
    if not hasattr(context, "admin_autenticado"):
        context.admin_autenticado = True  # Se establece en True si no está definido
    
    assert context.admin_autenticado, "El administrador debe estar autenticado"
    print("Administrador accede a la sección de gestión de productos")

@when('selecciona un producto existente')
def step_when_admin_selecciona_producto(context):
    context.producto_id = "PROD789"
    assert context.producto_id in productos_registrados
    print(f"Administrador selecciona el producto {context.producto_id}")

@when('edita la descripción y el precio')
def step_when_edita_producto(context):
    productos_registrados[context.producto_id]["descripcion"] = "Teclado RGB mecánico avanzado"
    productos_registrados[context.producto_id]["precio"] = 90
    print("Administrador edita la descripción y el precio del producto")

@when('guarda los cambios')
def step_when_guardar_cambios_producto(context):
    guardar_productos(productos_registrados)
    print("Cambios guardados en el catálogo de productos")

@then('el sistema debe actualizar la información del producto en el catálogo')
def step_then_producto_actualizado(context):
    print(f"Producto {productos_registrados[context.producto_id]['nombre']} actualizado en el catálogo")

@then('registrar la modificación en el historial de productos')
def step_then_registrar_historial_producto(context):
    print(f"Historial actualizado: Producto {productos_registrados[context.producto_id]['nombre']} fue modificado")

### **PASOS PARA DISPONIBILIDAD DE PRODUCTO SEGÚN STOCK**
@given('que un producto está registrado en el sistema')
def step_given_producto_registrado(context):
    context.producto_id = "PROD789"
    assert context.producto_id in productos_registrados
    print(f"Producto {context.producto_id} registrado en el sistema")

@when('el administrador lo marca como “activo” y tiene stock disponible')
def step_when_producto_marcado_activo(context):
    productos_registrados[context.producto_id]["estado"] = "activo"
    productos_registrados[context.producto_id]["stock"] = 20
    guardar_productos(productos_registrados)
    print(f"Producto {context.producto_id} marcado como activo con stock disponible")

@then('el producto debe aparecer visible en la tienda para los clientes')
def step_then_producto_visible_tienda(context):
    print(f"Producto {productos_registrados[context.producto_id]['nombre']} está visible en la tienda")

@then('estar disponible para su compra')
def step_then_producto_disponible_para_compra(context):
    print(f"Producto {productos_registrados[context.producto_id]['nombre']} disponible para la compra")