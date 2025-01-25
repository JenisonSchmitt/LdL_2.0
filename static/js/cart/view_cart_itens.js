document.addEventListener('DOMContentLoaded', function() {
    function updateCartBadge() {
      const cart = JSON.parse(localStorage.getItem('cart')) || [];
      const cartBadge = document.getElementById('cart-badge');
      
      cartBadge.textContent = cart.length;
    }
  
    updateCartBadge();
  
    document.querySelectorAll('.btn-cart').forEach(button => {
      button.addEventListener('click', function() {
        updateCartBadge();
      });
    });
  });
  