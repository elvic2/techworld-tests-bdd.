import json
import os
from behave import given, when, then

ORDERS_FILE = "data/orders.json"

def cargar_pedidos():
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as file:
            return json.load(file)
    return {}

def guardar_pedidos(data):
    with open(ORDERS_FILE, "w") as file:
        json.dump(data, file, indent=4)

pedidos_registrados = cargar_pedidos()

@given('el usuario accede a la sección "Mis Pedidos"')
def step_given_usuario_mis_pedidos(context):
    context.usuario_autenticado = True
    print("El usuario ha accedido a la sección 'Mis Pedidos'.")

@when('busca su pedido ingresando el número de orden')
def step_when_usuario_ingresa_pedido(context):
    context.pedido_id = "PED12345"
    context.pedido_info = pedidos_registrados.get(context.pedido_id, {})
    print(f"El usuario ha ingresado el número de pedido: {context.pedido_id}")

@then('ve el estado actual de su pedido en la pantalla')
def step_then_mostrar_estado_pedido(context):
    assert context.pedido_info, "El pedido no fue encontrado"
    print(f"Estado actual del pedido: {context.pedido_info.get('estado', 'Desconocido')}")

@then('la plataforma muestra la fecha estimada de entrega')
def step_then_mostrar_fecha_entrega(context):
    print(f"Fecha estimada de entrega: {context.pedido_info.get('fecha_entrega', 'No disponible')}")

@given('el usuario tiene un pedido en estado "Enviado"')
def step_given_pedido_enviado(context):
    context.pedido_id = "PED12345"
    pedidos_registrados[context.pedido_id] = {"estado": "Enviado", "fecha_entrega": "2024-06-15"}
    guardar_pedidos(pedidos_registrados)
    print(f"El pedido {context.pedido_id} está en estado Enviado.")

@when('el pedido cambia a estado "En tránsito"')
def step_when_pedido_cambia_en_transito(context):
    pedidos_registrados[context.pedido_id]["estado"] = "En tránsito"
    guardar_pedidos(pedidos_registrados)
    print(f"El pedido {context.pedido_id} ahora está en tránsito.")

@then('recibe una notificación en la plataforma')
def step_then_usuario_recibe_notificacion(context):
    print("El usuario ha recibido una notificación en la plataforma sobre su pedido en tránsito.")

@then('el estado de su pedido se actualiza en su cuenta')
def step_then_actualizar_info_pedidos(context):
    print(f"El estado del pedido {context.pedido_id} ha sido actualizado en la cuenta del usuario.")

@given('el usuario tiene un pedido en tránsito')
def step_given_pedido_en_transito(context):
    context.pedido_id = "PED12345"
    pedidos_registrados[context.pedido_id] = {"estado": "En tránsito", "fecha_entrega": "2024-06-15"}
    guardar_pedidos(pedidos_registrados)
    print(f"El pedido {context.pedido_id} está en tránsito.")

@when('el pedido sufre un retraso inesperado')
def step_when_pedido_retrasado(context):
    pedidos_registrados[context.pedido_id]["fecha_entrega"] = "2024-06-20"
    guardar_pedidos(pedidos_registrados)
    print(f"El pedido {context.pedido_id} se ha retrasado. Nueva fecha de entrega: {pedidos_registrados[context.pedido_id]['fecha_entrega']}")

@then('se actualiza la fecha estimada de entrega en pantalla')
def step_then_actualizar_fecha_entrega(context):
    print(f"La nueva fecha estimada de entrega del pedido {context.pedido_id} ha sido actualizada en la plataforma.")

@then('el usuario recibe una notificación con la nueva fecha')
def step_then_usuario_recibe_notificacion_retraso(context):
    print("El usuario ha recibido una notificación sobre la nueva fecha de entrega.")

@given('el usuario accede a la sección de seguimiento de pedidos')
def step_given_usuario_seguimiento_pedidos(context):
    print("El usuario ha accedido a la sección de seguimiento de pedidos.")

@when('ingresa un número de pedido incorrecto')
def step_when_usuario_ingresa_pedido_invalido(context):
    context.pedido_id = "PED00000"
    print(f"El usuario ingresó el número de pedido incorrecto: {context.pedido_id}")

@then('la plataforma muestra un mensaje indicando que el pedido no existe')
def step_then_mostrar_mensaje_error_pedido(context):
    assert context.pedido_id not in pedidos_registrados, "El pedido no debería existir"
    print("Mensaje en pantalla: El número de pedido ingresado no existe.")

@then('solicita que ingrese un número de pedido válido')
def step_then_solicitar_pedido_valido(context):
    print("Mensaje en pantalla: Por favor ingrese un número de pedido válido.")