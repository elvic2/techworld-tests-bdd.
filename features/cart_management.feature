Feature: Gestión del carrito de compras y wishlist
  Como cliente, quiero poder agregar productos a mi carrito de compras o a una wishlist,
  para poder comprarlos en el momento que desee.

  Scenario: Agregar un producto al carrito de compras
    Given que un usuario autenticado está navegando por el catálogo
    When selecciona un producto y hace clic en "Agregar al carrito"
    Then el sistema debe agregar el producto al carrito
    And mostrar un mensaje de confirmación del carrito

  Scenario: Modificación de la cantidad de productos en el carrito
    Given que un usuario tiene productos en su carrito
    When modifica la cantidad de un producto
    Then el sistema debe recalcular el total del carrito
    And reflejar los cambios en el resumen del pedido

  Scenario: Almacenamiento de un producto en la wishlist
    Given que un usuario autenticado está en la página de un producto
    When hace clic en "Agregar a wishlist"
    Then el producto debe almacenarse en su lista de deseos
    And ser accesible desde la sección "Mi Wishlist"

  Scenario: Notificación de stock bajo en la wishlist
    Given que un usuario tiene productos en su wishlist
    When un producto de la lista queda sin stock
    Then el sistema debe enviar una notificación de stock en wishlist
    And mostrar un mensaje de advertencia en la wishlist