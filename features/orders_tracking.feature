Feature: Seguimiento de Pedidos
  Como cliente, quiero rastrear mi pedido en tiempo real,
  para conocer su ubicación y la fecha estimada de entrega.

  Scenario: Seguimiento exitoso de un pedido
    Given el usuario accede a la sección "Mis Pedidos"
    When busca su pedido ingresando el número de orden
    Then ve el estado actual de su pedido en la pantalla
    And la plataforma muestra la fecha estimada de entrega

  Scenario: Pedido en tránsito con notificación al usuario
    Given el usuario tiene un pedido en estado "Enviado"
    When el pedido cambia a estado "En tránsito"
    Then recibe una notificación en la plataforma
    And el estado de su pedido se actualiza en su cuenta

  Scenario: Pedido retrasado con alerta de actualización
    Given el usuario tiene un pedido en tránsito
    When el pedido sufre un retraso inesperado
    Then se actualiza la fecha estimada de entrega en pantalla
    And el usuario recibe una notificación con la nueva fecha

  Scenario: Intento de consulta con número de pedido inválido
    Given el usuario accede a la sección de seguimiento de pedidos
    When ingresa un número de pedido incorrecto
    Then la plataforma muestra un mensaje indicando que el pedido no existe
    And solicita que ingrese un número de pedido válido