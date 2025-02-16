import json
import os
from behave import given, when, then

CART_FILE = "data/cart.json"
WISHLIST_FILE = "data/wishlist.json"

def cargar_datos(file):
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return {}

def guardar_datos(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

carrito = cargar_datos(CART_FILE)
wishlist = cargar_datos(WISHLIST_FILE)

@given('el usuario está viendo un producto en la tienda')
def step_given_usuario_viendo_producto(context):
    context.producto = {"id": "PROD123", "nombre": "Laptop Gamer", "precio": 1500, "cantidad": 1}
    print(f"El usuario está viendo el producto: {context.producto['nombre']}")

@when('hace clic en "Agregar al carrito"')
def step_when_usuario_agrega_al_carrito(context):
    carrito[context.producto["id"]] = context.producto
    guardar_datos(CART_FILE, carrito)
    print(f"El usuario agregó {context.producto['nombre']} al carrito.")

@then('el producto aparece en su carrito de compras')
def step_then_producto_en_carrito(context):
    assert context.producto["id"] in carrito
    print(f"{context.producto['nombre']} está en el carrito.")

@then('recibe una confirmación en pantalla')
def step_then_mostrar_mensaje_carrito(context):
    print("Mensaje en pantalla: Producto agregado correctamente al carrito.")

@given('el usuario tiene productos en su carrito')
def step_given_usuario_con_productos_carrito(context):
    assert carrito, "El carrito está vacío"
    print("El usuario tiene productos en su carrito.")

@when('cambia la cantidad de un producto')
def step_when_usuario_modifica_cantidad(context):
    producto_id = "PROD123"
    if producto_id in carrito:
        carrito[producto_id]["cantidad"] = 2
        guardar_datos(CART_FILE, carrito)
    print(f"El usuario cambió la cantidad de {carrito[producto_id]['nombre']} a {carrito[producto_id]['cantidad']}.")

@then('el total del carrito se actualiza automáticamente')
def step_then_actualizar_total_carrito(context):
    total = sum(p["precio"] * p["cantidad"] for p in carrito.values())
    print(f"El nuevo total del carrito es: ${total}")

@then('el resumen del pedido refleja los cambios')
def step_then_actualizar_resumen_pedido(context):
    print("El resumen del pedido se ha actualizado.")

@given('el usuario está viendo un producto que le interesa')
def step_given_usuario_viendo_producto_interes(context):
    context.producto = {"id": "PROD456", "nombre": "Monitor 4K", "precio": 500}
    print(f"El usuario está viendo el producto: {context.producto['nombre']}")

@when('hace clic en "Agregar a wishlist"')
def step_when_usuario_agrega_wishlist(context):
    wishlist[context.producto["id"]] = context.producto
    guardar_datos(WISHLIST_FILE, wishlist)
    print(f"El usuario agregó {context.producto['nombre']} a la wishlist.")

@then('el producto aparece en su lista de deseos')
def step_then_producto_en_wishlist(context):
    assert context.producto["id"] in wishlist
    print(f"{context.producto['nombre']} está en la wishlist.")

@then('puede verlo en la sección "Mi Wishlist"')
def step_then_acceder_wishlist(context):
    print("El usuario puede ver su wishlist en la plataforma.")

@given('el usuario tiene productos en su wishlist')
def step_given_usuario_con_productos_wishlist(context):
    assert wishlist, "La wishlist está vacía"
    print("El usuario tiene productos guardados en su wishlist.")

@when('uno de los productos se queda sin stock')
def step_when_producto_sin_stock(context):
    producto_id = "PROD456"
    if producto_id in wishlist:
        wishlist[producto_id]["stock"] = 0
        guardar_datos(WISHLIST_FILE, wishlist)
    print(f"{wishlist[producto_id]['nombre']} se quedó sin stock.")

@then('recibe una notificación de alerta')
def step_then_usuario_recibe_alerta(context):
    print(f"Notificación en plataforma: {wishlist['PROD456']['nombre']} está fuera de stock.")

@then('en su wishlist aparece un mensaje de "Sin stock"')
def step_then_mensaje_sin_stock(context):
    print("Mensaje en pantalla: Este producto ya no está disponible.")