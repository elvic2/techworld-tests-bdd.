Feature: Registro y autenticación de usuarios
  Como usuario, quiero poder registrarme e iniciar sesión en la plataforma
  utilizando un formulario con validación de datos o autenticación mediante
  redes sociales, para acceder a funcionalidades personalizadas y realizar compras de manera segura.

  Scenario: Registro exitoso de un nuevo usuario
    Given que un usuario accede a la página de registro
    When completa todos los campos obligatorios con información válida
    And confirma su registro
    Then el sistema debe enviar un correo de verificación
    And mostrar un mensaje de confirmación de autenticación

  Scenario: Intento de registro con datos inválidos
    Given que un usuario intenta registrarse
    When ingresa un correo electrónico en formato incorrecto
    And una contraseña que no cumple con los requisitos mínimos
    Then el sistema debe mostrar mensajes de error
    And evitar el registro hasta corregir los datos

  Scenario: Inicio de sesión exitoso con credenciales correctas
    Given que un usuario tiene una cuenta registrada y activada
    When ingresa su correo y contraseña correctos en la página de inicio de sesión
    Then el sistema debe autenticar al usuario
    And redirigirlo a la página principal de su cuenta

  Scenario: Intento de inicio de sesión fallido con credenciales incorrectas
    Given que un usuario intenta iniciar sesión
    When ingresa credenciales incorrectas tres veces consecutivas
    Then el sistema debe bloquear temporalmente la cuenta
    And mostrar un mensaje indicando el bloqueo