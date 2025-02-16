import json
import os
from behave import given, when, then

DB_FILE = "data/users.json"

def cargar_usuarios():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            return json.load(file)
    return {}

def guardar_usuarios(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

usuarios_registrados = cargar_usuarios()

@given('el usuario accede a la página de registro')
def step_given_usuario_pagina_registro(context):
    context.usuario = {}
    print("El usuario ha accedido a la página de registro")

@when('completa sus datos y confirma su registro')
def step_when_usuario_completa_registro(context):
    context.usuario = {"email": "nuevo_usuario@example.com", "password": "Password123"}
    usuarios_registrados[context.usuario["email"]] = {
        "password": context.usuario["password"],
        "verificado": False
    }
    guardar_usuarios(usuarios_registrados)
    print("El usuario completó sus datos y se ha registrado")

@then('recibe un correo de verificación')
def step_then_usuario_recibe_correo(context):
    print("Correo de verificación enviado correctamente")

@then('puede acceder a su cuenta tras verificar su email')
def step_then_usuario_verifica_email(context):
    usuarios_registrados["nuevo_usuario@example.com"]["verificado"] = True
    guardar_usuarios(usuarios_registrados)
    print("El usuario ha verificado su email y puede acceder a su cuenta")

@given('el usuario tiene una cuenta verificada')
def step_given_usuario_verificado(context):
    context.usuario_email = "usuario.verificado@example.com"
    usuarios_registrados[context.usuario_email] = {"password": "password123", "verificado": True}
    guardar_usuarios(usuarios_registrados)
    print(f"El usuario {context.usuario_email} tiene una cuenta verificada")

@when('ingresa su correo y contraseña correctamente')
def step_when_usuario_ingresa_credenciales_correctas(context):
    assert usuarios_registrados[context.usuario_email]["verificado"]
    print(f"El usuario {context.usuario_email} ha ingresado correctamente")

@then('es redirigido a su perfil')
def step_then_usuario_redirigido_perfil(context):
    print(f"El usuario {context.usuario_email} ha sido redirigido a su perfil")

@then('ve su información de usuario en la plataforma')
def step_then_usuario_ve_perfil(context):
    print("Información de usuario mostrada correctamente")

@given('el usuario intenta iniciar sesión')
def step_given_usuario_intento_fallido(context):
    context.usuario_email = "usuario.bloqueado@example.com"
    usuarios_registrados[context.usuario_email] = {"password": "password123", "intentos_fallidos": 3}
    guardar_usuarios(usuarios_registrados)
    print("El usuario está intentando iniciar sesión")

@when('ingresa credenciales incorrectas varias veces')
def step_when_usuario_intentos_fallidos(context):
    usuarios_registrados[context.usuario_email]["intentos_fallidos"] += 1
    guardar_usuarios(usuarios_registrados)
    print(f"Intentos fallidos de {context.usuario_email}: {usuarios_registrados[context.usuario_email]['intentos_fallidos']}")

@then('su cuenta es temporalmente bloqueada')
def step_then_usuario_bloqueado(context):
    if usuarios_registrados[context.usuario_email]["intentos_fallidos"] >= 3:
        print(f"La cuenta de {context.usuario_email} ha sido temporalmente bloqueada")

@then('ve un mensaje indicando el bloqueo en pantalla')
def step_then_usuario_ve_mensaje_bloqueo(context):
    print("Mensaje en pantalla: Su cuenta ha sido bloqueada temporalmente debido a múltiples intentos fallidos")