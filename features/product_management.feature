Feature: Gestión de Productos en la Plataforma de E-commerce
  Como administrador, quiero gestionar los productos en la tienda,
  para mantener el catálogo actualizado y disponible para los clientes.

  Scenario: Creación de un nuevo producto
    Given el administrador accede a la sección de gestión de productos
    When completa los datos y guarda el nuevo producto
    Then el producto se agrega al catálogo
    And los clientes pueden verlo en la tienda

  Scenario: Intento de creación con datos incompletos
    Given el administrador intenta registrar un producto nuevo
    When deja un campo obligatorio vacío
    Then la plataforma muestra un mensaje de error
    And evita guardar el producto hasta completar los datos requeridos

  Scenario: Modificación de atributos de un producto existente
    Given el administrador accede a la lista de productos
    When edita la descripción y el precio de un producto
    And guarda los cambios
    Then la información del producto se actualiza en el catálogo
    And el historial de modificaciones se registra correctamente

  Scenario: Disponibilidad de producto en función del stock
    Given un producto está registrado en la tienda
    When el administrador lo activa y tiene stock disponible
    Then el producto se muestra en la tienda para los clientes
    And está disponible para su compra