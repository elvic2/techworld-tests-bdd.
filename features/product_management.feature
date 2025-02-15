Feature: Gestión de productos en la plataforma de e-commerce
  Como administrador, quiero poder crear, modificar y gestionar los atributos de los productos en la plataforma,
  para mantener el catálogo actualizado y disponible para la compra de los clientes.

  Scenario: Creación exitosa de un nuevo producto
    Given que el administrador ha iniciado sesión en la plataforma
    When accede a la sección de gestión de productos
    And completa los campos obligatorios (nombre, descripción, precio, stock, categoría)
    And guarda el producto
    Then el sistema debe registrar el nuevo producto en el catálogo
    And mostrar un mensaje de confirmación de creación de producto

  Scenario: Intento de creación con datos incompletos
    Given que el administrador intenta agregar un producto nuevo
    When omite un campo obligatorio
    Then el sistema debe mostrar un mensaje de error en la creación de producto
    And evitar la creación del producto hasta completar la información requerida

  Scenario: Modificación de atributos de un producto existente
    Given que el administrador está en la sección de gestión de productos
    When selecciona un producto existente
    And edita la descripción y el precio
    And guarda los cambios
    Then el sistema debe actualizar la información del producto en el catálogo
    And registrar la modificación en el historial de productos

  Scenario: Disponibilidad de producto en función del stock
    Given que un producto está registrado en el sistema
    When el administrador lo marca como “activo” y tiene stock disponible
    Then el producto debe aparecer visible en la tienda para los clientes
    And estar disponible para su compra