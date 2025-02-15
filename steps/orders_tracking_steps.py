import json
import os
from behave import given, when, then

ORDERS_FILE = "orders.json"

def cargar_pedidos():
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as file:
            return json.load(file)
    return {}

def guardar_pedidos(data):
    with open(ORDERS_FILE, "w") as file:
        json.dump(data, file, indent=4)

pedidos_registrados = cargar_pedidos()

### **PASOS PARA VISUALIZACIÓN DEL ESTADO DE PEDIDO**
@given('que un usuario autenticado accede a la sección "Mis Pedidos"')
def step_given_usuario_accede_mis_pedidos(context):
    context.usuario_autenticado = True
    print("Usuario autenticado accede a la sección de pedidos")

@when('ingresa un número de pedido válido')
def step_when_ingresa_numero_pedido_valido(context):
    context.pedido_id = "PED12345"
    context.pedido_info = pedidos_registrados.get(context.pedido_id, {})
    print(f"Pedido ingresado: {context.pedido_id}")

@then('el sistema debe mostrar el estado actual del pedido')
def step_then_mostrar_estado_pedido(context):
    assert context.pedido_info, "El pedido no fue encontrado"
    print(f"Estado actual del pedido: {context.pedido_info.get('estado', 'Desconocido')}")

@then('la fecha estimada de entrega')
def step_then_mostrar_fecha_entrega(context):
    print(f"Fecha estimada de entrega: {context.pedido_info.get('fecha_entrega', 'No disponible')}")

### **PASOS PARA PEDIDO EN TRÁNSITO**
@given('que el usuario tiene un pedido en estado "Enviado"')
def step_given_pedido_enviado(context):
    context.pedido_id = "PED12345"
    pedidos_registrados[context.pedido_id] = {"estado": "Enviado", "fecha_entrega": "2024-06-15"}
    guardar_pedidos(pedidos_registrados)
    print(f"Pedido {context.pedido_id} en estado Enviado")

@when('el pedido cambia a estado "En tránsito"')
def step_when_pedido_cambia_en_transito(context):
    pedidos_registrados[context.pedido_id]["estado"] = "En tránsito"
    guardar_pedidos(pedidos_registrados)
    print(f"Pedido {context.pedido_id} cambiado a En tránsito")

@then('el sistema debe enviar una notificación de actualización de pedido')
def step_then_enviar_notificacion_pedido(context):
    print(f"Notificación enviada: Su pedido {context.pedido_id} está en tránsito")

@then('actualizar la información en la sección de pedidos')
def step_then_actualizar_info_pedidos(context):
    print(f"Información del pedido {context.pedido_id} actualizada en el sistema")

### **PASOS PARA PEDIDO RETRASADO**
@given('que el usuario tiene un pedido en tránsito')
def step_given_pedido_en_transito(context):
    context.pedido_id = "PED12345"
    pedidos_registrados[context.pedido_id] = {"estado": "En tránsito", "fecha_entrega": "2024-06-15"}
    guardar_pedidos(pedidos_registrados)
    print(f"Pedido {context.pedido_id} está en tránsito")

@when('el pedido sufre un retraso')
def step_when_pedido_retrasado(context):
    pedidos_registrados[context.pedido_id]["fecha_entrega"] = "2024-06-20"
    guardar_pedidos(pedidos_registrados)
    print(f"Pedido {context.pedido_id} retrasado. Nueva fecha de entrega: {pedidos_registrados[context.pedido_id]['fecha_entrega']}")

@then('el sistema debe actualizar la fecha estimada de entrega')
def step_then_actualizar_fecha_entrega(context):
    print(f"Fecha estimada de entrega del pedido {context.pedido_id} actualizada")

@then('enviar una notificación con la nueva fecha')
def step_then_notificar_retraso(context):
    print(f"Notificación enviada: Su pedido {context.pedido_id} ha sido retrasado. Nueva fecha: {pedidos_registrados[context.pedido_id]['fecha_entrega']}")

### **PASOS PARA PEDIDO INVÁLIDO**
@given('que un usuario accede a la sección de seguimiento de pedidos')
def step_given_usuario_accede_seguimiento_pedidos(context):
    context.usuario_autenticado = True
    print("Usuario autenticado accede a la sección de seguimiento")

@when('ingresa un número de pedido incorrecto')
def step_when_ingresa_pedido_invalido(context):
    context.pedido_id = "PED00000"  # Simula un pedido que no existe
    print(f"Pedido ingresado: {context.pedido_id}")

@then('el sistema debe mostrar un mensaje de error')
def step_then_mostrar_mensaje_error_pedido(context):
    assert context.pedido_id not in pedidos_registrados, "El pedido no debería existir"
    print("Error: Pedido no encontrado")

@then('solicitar un número de pedido válido')
def step_then_solicitar_pedido_valido(context):
    print("Por favor ingrese un número de pedido válido")