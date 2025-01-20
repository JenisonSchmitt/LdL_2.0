document.addEventListener('DOMContentLoaded', function() {
    // Função para atualizar o número de itens no carrinho
    function updateCartBadge() {
      const cart = JSON.parse(localStorage.getItem('cart')) || [];
      const cartBadge = document.getElementById('cart-badge');
      
      // Atualiza o texto do badge com a quantidade de itens no carrinho
      cartBadge.textContent = cart.length;
    }
  
    // Chama a função para inicializar o badge
    updateCartBadge();
  
    // Adiciona um ouvinte de evento para atualizar o badge sempre que um item for adicionado ao carrinho
    document.querySelectorAll('.btn-cart').forEach(button => {
      button.addEventListener('click', function() {
        // Supondo que o item já foi adicionado ao carrinho no localStorage
        updateCartBadge();
      });
    });
  });
  