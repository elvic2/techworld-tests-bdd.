Feature: Gestión del Carrito de Compras y Wishlist
  Como cliente, quiero agregar productos a mi carrito y lista de deseos,
  para poder comprarlos en el momento que desee.

  Scenario: Agregar un producto al carrito
    Given el usuario está viendo un producto en la tienda
    When hace clic en "Agregar al carrito"
    Then el producto aparece en su carrito de compras
    And recibe una confirmación en pantalla

  Scenario: Modificación de la cantidad de productos en el carrito
    Given el usuario tiene productos en su carrito
    When cambia la cantidad de un producto
    Then el total del carrito se actualiza automáticamente
    And el resumen del pedido refleja los cambios

  Scenario: Guardar un producto en la wishlist
    Given el usuario está viendo un producto que le interesa
    When hace clic en "Agregar a wishlist"
    Then el producto aparece en su lista de deseos
    And puede verlo en la sección "Mi Wishlist"

  Scenario: Notificación de stock bajo en la wishlist
    Given el usuario tiene productos en su wishlist
    When uno de los productos se queda sin stock
    Then recibe una notificación de alerta
    And en su wishlist aparece un mensaje de "Sin stock"