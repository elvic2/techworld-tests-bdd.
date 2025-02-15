Feature: Seguimiento de pedidos en tiempo real
  Como cliente, quiero poder rastrear mi pedido en tiempo real,
  para conocer su ubicación y la fecha estimada de entrega.

  Scenario: Visualización exitosa del estado de un pedido
    Given que un usuario autenticado accede a la sección "Mis Pedidos"
    When ingresa un número de pedido válido
    Then el sistema debe mostrar el estado actual del pedido
    And la fecha estimada de entrega

  Scenario: Pedido en tránsito con notificación al usuario
    Given que el usuario tiene un pedido en estado "Enviado"
    When el pedido cambia a estado "En tránsito"
    Then el sistema debe enviar una notificación de actualización de pedido
    And actualizar la información en la sección de pedidos

  Scenario: Pedido retrasado con alerta de actualización
    Given que el usuario tiene un pedido en tránsito
    When el pedido sufre un retraso
    Then el sistema debe actualizar la fecha estimada de entrega
    And enviar una notificación con la nueva fecha

  Scenario: Intento de consulta con número de pedido inválido
    Given que un usuario accede a la sección de seguimiento de pedidos
    When ingresa un número de pedido incorrecto
    Then el sistema debe mostrar un mensaje de error
    And solicitar un número de pedido válido