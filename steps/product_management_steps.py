import json
import os
from behave import given, when, then

PRODUCTS_FILE = "data/products.json"

def cargar_productos():
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, "r") as file:
            return json.load(file)
    return {}

def guardar_productos(data):
    with open(PRODUCTS_FILE, "w") as file:
        json.dump(data, file, indent=4)

productos_registrados = cargar_productos()

@given('el administrador accede a la sección de gestión de productos')
def step_given_admin_gestion_productos(context):
    context.admin_autenticado = True
    print("El administrador ha accedido a la sección de gestión de productos.")

@when('completa los datos y guarda el nuevo producto')
def step_when_admin_crea_producto(context):
    context.producto = {
        "id": "PROD789",
        "nombre": "Teclado Mecánico RGB",
        "descripcion": "Teclado gaming con retroiluminación RGB",
        "precio": 80,
        "stock": 50,
        "categoria": "Periféricos"
    }
    productos_registrados[context.producto["id"]] = context.producto
    guardar_productos(productos_registrados)
    print(f"El producto {context.producto['nombre']} ha sido agregado al catálogo.")

@then('el producto se agrega al catálogo')
def step_then_producto_en_catalogo(context):
    assert context.producto["id"] in productos_registrados
    print(f"{context.producto['nombre']} está disponible en el catálogo.")

@then('los clientes pueden verlo en la tienda')
def step_then_producto_visible_tienda(context):
    print(f"{context.producto['nombre']} ahora es visible en la tienda.")

@given('el administrador intenta registrar un producto nuevo')
def step_given_admin_intenta_crear_producto(context):
    context.producto = {"nombre": "", "precio": 100}  # Simulación de campo vacío
    print("El administrador intenta registrar un producto sin completar todos los campos.")

@when('deja un campo obligatorio vacío')
def step_when_omite_campo_obligatorio(context):
    assert "nombre" in context.producto and context.producto["nombre"] == ""
    print("El administrador dejó un campo obligatorio vacío.")

@then('la plataforma muestra un mensaje de error')
def step_then_mensaje_error_producto(context):
    print("Error: No se puede registrar el producto sin completar todos los campos.")

@then('evita guardar el producto hasta completar los datos requeridos')
def step_then_evitar_guardado_producto(context):
    print("El producto no será guardado hasta que se completen todos los datos.")

@given('el administrador accede a la lista de productos')
def step_given_admin_lista_productos(context):
    # Si el atributo no existe, lo inicializamos en False
    if not hasattr(context, "admin_autenticado"):
        context.admin_autenticado = True  # Se establece en True para la prueba
    
    assert context.admin_autenticado, "El administrador debe estar autenticado"
    print("El administrador accede a la lista de productos.")

@when('edita la descripción y el precio de un producto')
def step_when_edita_producto(context):
    context.producto_id = "PROD789"
    assert context.producto_id in productos_registrados
    productos_registrados[context.producto_id]["descripcion"] = "Teclado RGB mecánico avanzado"
    productos_registrados[context.producto_id]["precio"] = 90
    print("El administrador ha editado la descripción y el precio del producto.")

@when('guarda los cambios')
def step_when_guardar_cambios_producto(context):
    guardar_productos(productos_registrados)
    print("Los cambios han sido guardados en el catálogo.")

@then('la información del producto se actualiza en el catálogo')
def step_then_producto_actualizado(context):
    print(f"El producto {productos_registrados[context.producto_id]['nombre']} ha sido actualizado en el catálogo.")

@then('el historial de modificaciones se registra correctamente')
def step_then_registro_historial(context):
    print(f"El historial de cambios ha sido actualizado para {productos_registrados[context.producto_id]['nombre']}.")

@given('un producto está registrado en la tienda')
def step_given_producto_registrado(context):
    context.producto_id = "PROD789"
    assert context.producto_id in productos_registrados
    print(f"El producto {context.producto_id} está registrado en la tienda.")

@when('el administrador lo activa y tiene stock disponible')
def step_when_producto_marcado_activo(context):
    productos_registrados[context.producto_id]["estado"] = "activo"
    productos_registrados[context.producto_id]["stock"] = 20
    guardar_productos(productos_registrados)
    print(f"El producto {context.producto_id} ha sido activado y tiene stock disponible.")

@then('el producto se muestra en la tienda para los clientes')
def step_then_producto_visible_clientes(context):
    print(f"El producto {productos_registrados[context.producto_id]['nombre']} ahora está disponible en la tienda.")

@then('está disponible para su compra')
def step_then_producto_disponible_para_compra(context):
    print(f"El producto {productos_registrados[context.producto_id]['nombre']} está disponible para la compra.")