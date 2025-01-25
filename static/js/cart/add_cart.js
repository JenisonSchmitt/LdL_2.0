document.addEventListener('DOMContentLoaded', function() {
  // Adiciona evento para o botão de adicionar ao carrinho
  document.querySelectorAll('.btn-cart').forEach(function(button) {
    button.addEventListener('click', function(event) {
      event.preventDefault();

      const productId = this.getAttribute('data-id');
      const productName = this.getAttribute('data-name');
      const productPrice = parseFloat(this.getAttribute('data-price'));

      let cart = JSON.parse(localStorage.getItem('cart')) || [];

      // Verifica se o item já existe no carrinho
      const existingProduct = cart.find(product => product.id === productId);

      if (existingProduct) {
        existingProduct.quantity += 1;
      } else {
        cart.push({ id: productId, name: productName, price: productPrice, quantity: 1 });
      }

      // Salva no localStorage e atualiza a interface do carrinho
      localStorage.setItem('cart', JSON.stringify(cart));
      updateCart();

      showSuccessNotification();
    });
  });

  // Função de atualização do carrinho
  function updateCart() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const cartCount = document.querySelector('.badge.bg-primary');
    const cartItemsList = document.querySelector('.offcanvas-body .list-group');

    if (cartCount) {
      cartCount.textContent = cart.length;
    }

    if (cartItemsList) {
      cartItemsList.innerHTML = '';
      let total = 0;
      let productIds = [];
      let productQuantities = [];

      cart.forEach(product => {
        const productTotal = product.price * product.quantity;
        total += productTotal;

        const listItem = document.createElement('li');
        listItem.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'lh-sm');
        listItem.innerHTML = `
          <div class="d-flex justify-content-between w-100">
            <div>
              <h6 class="my-0">${product.name} (x${product.quantity})</h6>
            </div>
          </div>
          <span class="text-body-secondary">R$ ${productTotal.toFixed(2)}</span>
          <button class="btn btn-sm btn-danger delete-item" data-id="${product.id}">
              <iconify-icon icon="fluent:delete-16-regular"></iconify-icon>
          </button>
        `;
        cartItemsList.appendChild(listItem);

        productIds.push(product.id);
        productQuantities.push(product.quantity);
      });

      // Exibe o valor total do carrinho
      cartItemsList.innerHTML += ` 
        <li class="list-group-item d-flex justify-content-between">
          <span class="fw-bold">Total</span>
          <strong>R$ ${total.toFixed(2)}</strong>
        </li>
      `;
      document.getElementById('product-ids').value = JSON.stringify(productIds);
      document.getElementById('product-quantities').value = JSON.stringify(productQuantities);
    }

    // Adiciona evento para remover item
    document.querySelectorAll('.delete-item').forEach(function(button) {
      button.addEventListener('click', function() {
        const productId = this.getAttribute('data-id');
        removeFromCart(productId);
      });
    });
  }

  // Função de remoção de produto do carrinho
  function removeFromCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart = cart.filter(product => product.id !== productId);
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCart();
  }
  
  // Carrega o carrinho ao abrir a página
  updateCart();
});
