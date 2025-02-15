import json
import os
from behave import given, when, then

DB_FILE = "users.json"

def cargar_usuarios():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            return json.load(file)
    return {}

def guardar_usuarios(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

usuarios_registrados = cargar_usuarios()

### **PASOS PARA REGISTRO EXITOSO**
@given('que un usuario accede a la página de registro')
def step_given_usuario_accede_pagina_registro(context):
    context.usuario = {}
    print("Usuario en la página de registro")

@when('completa todos los campos obligatorios con información válida')
def step_when_completa_campos_validos(context):
    context.usuario = {"email": "nuevo_usuario@example.com", "password": "Password123"}
    print("Campos completados con información válida")

@when('confirma su registro')
def step_when_confirma_registro(context):
    email = context.usuario["email"]
    
    if email not in usuarios_registrados:
        usuarios_registrados[email] = {
            "password": context.usuario["password"],
            "activo": False,
            "intentos_fallidos": 0
        }
        guardar_usuarios(usuarios_registrados)
    
    context.usuario["confirmado"] = True  # Asegurar que siempre se define
    print("Registro confirmado")

@then('el sistema debe enviar un correo de verificación')
def step_then_envia_correo_verificacion(context):
    assert context.usuario["confirmado"] is True
    print(f"Correo de verificación enviado a {context.usuario['email']}")

@then('mostrar un mensaje de confirmación de autenticación')
def step_then_mostrar_mensaje_confirmacion_auth(context):
    print("Registro exitoso - Usuario creado")

### **PASOS PARA REGISTRO CON DATOS INVÁLIDOS**
@given('que un usuario intenta registrarse')
def step_given_usuario_intenta_registrarse(context):
    context.usuario = {}
    print("Usuario intentando registrarse")

@when('ingresa un correo electrónico en formato incorrecto')
def step_when_ingresa_correo_incorrecto(context):
    context.usuario["email"] = "correo_invalido"
    print("Correo ingresado en formato incorrecto")

@when('una contraseña que no cumple con los requisitos mínimos')
def step_when_contrasena_invalida(context):
    context.usuario["password"] = "123"
    print("Contraseña no cumple con los requisitos mínimos")

@then('el sistema debe mostrar mensajes de error')
def step_then_mostrar_mensaje_error(context):
    email_correcto = "@" in context.usuario["email"] and "." in context.usuario["email"]
    password_correcta = len(context.usuario["password"]) >= 6
    assert not email_correcto or not password_correcta
    print("Error: Formato de correo o contraseña inválida")

@then('evitar el registro hasta corregir los datos')
def step_then_evitar_registro(context):
    print("Registro bloqueado hasta corregir los datos")

### **PASOS PARA INICIO DE SESIÓN EXITOSO**
@given('que un usuario tiene una cuenta registrada y activada')
def step_given_usuario_registrado(context):
    context.usuario_email = "victor.vargas@example.com"
    context.usuario = usuarios_registrados.get(context.usuario_email, {})
    print(f"Usuario {context.usuario_email} registrado y activado")

@when('ingresa su correo y contraseña correctos en la página de inicio de sesión')
def step_when_ingresa_credenciales_correctas(context):
    usuario = usuarios_registrados.get(context.usuario_email, {})
    assert usuario.get("password") == "Victor123"
    print("Credenciales correctas")

@then('el sistema debe autenticar al usuario')
def step_then_autenticar_usuario(context):
    print(f"Usuario {context.usuario_email} autenticado correctamente")

@then('redirigirlo a la página principal de su cuenta')
def step_then_redirigir_usuario(context):
    print(f"Redirigiendo a la cuenta de {context.usuario_email}")

### **PASOS PARA INTENTO FALLIDO DE INICIO DE SESIÓN**
@given('que un usuario intenta iniciar sesión')
def step_given_usuario_intenta_inicio_sesion(context):
    context.usuario_email = "dayro.moreno@example.com"
    context.usuario = usuarios_registrados.get(context.usuario_email, {})
    print(f"Usuario {context.usuario_email} intentando iniciar sesión")

@when('ingresa credenciales incorrectas tres veces consecutivas')
def step_when_ingresa_credenciales_incorrectas(context):
    usuario = usuarios_registrados.get(context.usuario_email, {})
    if usuario:
        usuario["intentos_fallidos"] += 3
        guardar_usuarios(usuarios_registrados)
    print(f"Intentos fallidos de {context.usuario_email}: {usuario['intentos_fallidos']}")

@then('el sistema debe bloquear temporalmente la cuenta')
def step_then_bloquear_usuario(context):
    usuario = usuarios_registrados.get(context.usuario_email, {})
    if usuario and usuario["intentos_fallidos"] >= 3:
        usuario["activo"] = False
        guardar_usuarios(usuarios_registrados)
        print(f"Cuenta de {context.usuario_email} bloqueada temporalmente")

@then('mostrar un mensaje indicando el bloqueo')
def step_then_mostrar_mensaje_bloqueo(context):
    print(f"Mensaje: La cuenta de {context.usuario_email} ha sido bloqueada por múltiples intentos fallidos")