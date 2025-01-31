document.addEventListener('DOMContentLoaded', function() {
  function updateCartBadge() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const cartBadge = document.getElementById('cart-badge');
    if (cartBadge) {
      cartBadge.textContent = cart.length;
    }
    const cartBadge2 = document.getElementById('cart-badge-2');
    if (cartBadge2) {
      cartBadge2.textContent = cart.length;
    }
  }

  updateCartBadge();

  document.querySelectorAll('.btn-cart').forEach(button => {
    button.addEventListener('click', function() {
      updateCartBadge();
    });
  });
});
