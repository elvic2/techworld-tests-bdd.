Feature: Autenticación de Usuarios
  Como usuario, quiero poder registrarme e iniciar sesión en la plataforma,
  para acceder a funcionalidades personalizadas y realizar compras de manera segura.

  Scenario: Registro exitoso de un nuevo usuario
    Given el usuario accede a la página de registro
    When completa sus datos y confirma su registro
    Then recibe un correo de verificación
    And puede acceder a su cuenta tras verificar su email

  Scenario: Inicio de sesión exitoso
    Given el usuario tiene una cuenta verificada
    When ingresa su correo y contraseña correctamente
    Then es redirigido a su perfil
    And ve su información de usuario en la plataforma

  Scenario: Inicio de sesión fallido por credenciales incorrectas
    Given el usuario intenta iniciar sesión
    When ingresa credenciales incorrectas varias veces
    Then su cuenta es temporalmente bloqueada
    And ve un mensaje indicando el bloqueo en pantalla