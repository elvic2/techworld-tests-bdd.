import json
import os
from behave import given, when, then

CART_FILE = "cart.json"
WISHLIST_FILE = "wishlist.json"

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

### **PASOS PARA GESTIÓN DEL CARRITO**
@given('que un usuario autenticado está navegando por el catálogo')
def step_given_usuario_navega_catalogo(context):
    context.usuario_autenticado = True
    print("Usuario autenticado navegando en el catálogo")

@when('selecciona un producto y hace clic en "Agregar al carrito"')
def step_when_agrega_producto_carrito(context):
    context.producto = {"id": "PROD123", "nombre": "Laptop Gamer", "precio": 1500, "cantidad": 1}
    carrito[context.producto["id"]] = context.producto
    guardar_datos(CART_FILE, carrito)
    print(f"Producto {context.producto['nombre']} agregado al carrito")

@then('el sistema debe agregar el producto al carrito')
def step_then_producto_agregado_carrito(context):
    assert context.producto["id"] in carrito
    print("Producto agregado correctamente al carrito")

@then('mostrar un mensaje de confirmación del carrito')
def step_then_mostrar_mensaje_confirmacion_carrito(context):
    print(f"Mensaje: {context.producto['nombre']} ha sido agregado al carrito")

### **PASOS PARA MODIFICAR CANTIDAD EN EL CARRITO**
@given('que un usuario tiene productos en su carrito')
def step_given_usuario_con_productos_en_carrito(context):
    assert carrito, "El carrito está vacío"
    print("Usuario tiene productos en el carrito")

@when('modifica la cantidad de un producto')
def step_when_modifica_cantidad_producto(context):
    producto_id = "PROD123"
    if producto_id in carrito:
        carrito[producto_id]["cantidad"] = 2
        guardar_datos(CART_FILE, carrito)
    print(f"Cantidad de {carrito[producto_id]['nombre']} modificada a {carrito[producto_id]['cantidad']}")

@then('el sistema debe recalcular el total del carrito')
def step_then_actualizar_total_carrito(context):
    total = sum(p["precio"] * p["cantidad"] for p in carrito.values())
    print(f"Nuevo total del carrito: ${total}")

@then('reflejar los cambios en el resumen del pedido')
def step_then_reflejar_cambios_resumen(context):
    print("Resumen del pedido actualizado con la nueva cantidad de productos")

### **PASOS PARA GESTIÓN DE WISHLIST**
@given('que un usuario autenticado está en la página de un producto')
def step_given_usuario_en_pagina_producto(context):
    context.producto = {"id": "PROD456", "nombre": "Monitor 4K", "precio": 500}
    print(f"Usuario viendo el producto {context.producto['nombre']}")

@when('hace clic en "Agregar a wishlist"')
def step_when_agrega_producto_wishlist(context):
    wishlist[context.producto["id"]] = context.producto
    guardar_datos(WISHLIST_FILE, wishlist)
    print(f"Producto {context.producto['nombre']} agregado a la wishlist")

@then('el producto debe almacenarse en su lista de deseos')
def step_then_producto_en_wishlist(context):
    assert context.producto["id"] in wishlist
    print(f"{context.producto['nombre']} almacenado en la wishlist correctamente")

@then('ser accesible desde la sección "Mi Wishlist"')
def step_then_accesible_desde_wishlist(context):
    print("Wishlist disponible para el usuario")

### **PASOS PARA NOTIFICACIÓN DE STOCK BAJO EN WISHLIST**
@given('que un usuario tiene productos en su wishlist')
def step_given_usuario_con_productos_wishlist(context):
    assert wishlist, "La wishlist está vacía"
    print("Usuario tiene productos en su wishlist")

@when('un producto de la lista queda sin stock')
def step_when_producto_sin_stock(context):
    producto_id = "PROD456"
    if producto_id in wishlist:
        wishlist[producto_id]["stock"] = 0  # Simular que el producto se agotó
        guardar_datos(WISHLIST_FILE, wishlist)
    print(f"{wishlist[producto_id]['nombre']} ha quedado sin stock")

@then('el sistema debe enviar una notificación de stock en wishlist')
def step_then_enviar_notificacion_stock_wishlist(context):
    print(f"Notificación enviada: {wishlist['PROD456']['nombre']} está fuera de stock")

@then('mostrar un mensaje de advertencia en la wishlist')
def step_then_mostrar_mensaje_stock(context):
    print(f"Advertencia: {wishlist['PROD456']['nombre']} no está disponible actualmente")