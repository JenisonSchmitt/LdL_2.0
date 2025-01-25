document.addEventListener('DOMContentLoaded', function() {
    function updateCartBadge() {
      const cart = JSON.parse(localStorage.getItem('cart')) || [];
      const cartBadge = document.getElementById('cart-badge');
      
      cartBadge.textContent = cart.length;
    }
  
    updateCartBadge();
  
    const clearCartButton = document.getElementById('clear-cart');
    const clearCartModal = new bootstrap.Modal(document.getElementById('clearCartModal'));
  
    if (clearCartButton) {
      clearCartButton.addEventListener('click', function() {
        clearCartModal.show();
      });
    }
  
    const confirmClearCartButton = document.getElementById('confirm-clear-cart');
    if (confirmClearCartButton) {
      confirmClearCartButton.addEventListener('click', function() {
        localStorage.removeItem('cart');
  
        updateCartBadge();
  
        clearCartModal.hide();
  
        const successCartClearModal = new bootstrap.Modal(document.getElementById('successCartClearModal'));
        successCartClearModal.show();
        setTimeout(function() {
            location.reload();
        }, 2000);

      });
    }
  });
  