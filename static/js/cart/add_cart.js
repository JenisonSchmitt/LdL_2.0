document.addEventListener('DOMContentLoaded', function() {
  // Função para adicionar o produto ao carrinho
  document.querySelectorAll('.btn-cart').forEach(function(button) {
    button.addEventListener('click', function(event) {
      event.preventDefault();

      const productId = this.getAttribute('data-id');
      const productName = this.getAttribute('data-name');
      const productPrice = parseFloat(this.getAttribute('data-price'));

      let cart = JSON.parse(localStorage.getItem('cart')) || [];
      const existingProductIndex = cart.findIndex(product => product.id === productId);

      if (existingProductIndex >= 0) {
        cart[existingProductIndex].quantity += 1;
      } else {
        cart.push({ id: productId, name: productName, price: productPrice, quantity: 1 });
      }

      // Atualiza o carrinho no localStorage
      localStorage.setItem('cart', JSON.stringify(cart));

      // Chama a função de atualização do carrinho logo após a adição
      updateCart();

      showSuccessNotification();  // Exibe o modal de sucesso
    });
  });

  // Função para exibir o modal de sucesso
  function showSuccessNotification() {
    const successModal = new bootstrap.Modal(document.getElementById('successCartAddModal'));
    successModal.show();
  }

  function updateCart() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const cartCount = document.querySelector('.badge.bg-primary');
    const cartItemsList = document.querySelector('.offcanvas-body .list-group');

    console.log("updateCart chamado. Conteúdo do carrinho:", cart);

    if (cartCount) {
      cartCount.textContent = cart.length;
    }

    if (cartItemsList) {
      cartItemsList.innerHTML = ''; // Limpa a lista antes de adicionar os novos itens

      let total = 0;
      cart.forEach(product => {
        const productTotal = product.price * product.quantity;
        total += productTotal;

        // Criação de um item de carrinho
        const listItem = document.createElement('li');
        listItem.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'lh-sm');
        listItem.innerHTML = `
          <div class="d-flex justify-content-between w-100">
            <div>
              <h6 class="my-0">${product.name} (x${product.quantity})</h6>
              <small class="text-body-secondary">Brief description</small>
            </div>
          </div>
          <span class="text-body-secondary">R$ ${product.price.toFixed(2)}</span>
          <span class="text-body-secondary">Total: R$ ${productTotal.toFixed(2)}</span>
          <button class="btn btn-sm btn-danger delete-item" data-id="${product.id}">
              <iconify-icon icon="fluent:delete-16-regular"></iconify-icon>
          </button>
        `;

        cartItemsList.appendChild(listItem);
      });

      // Atualiza o total no carrinho
      const totalItem = document.querySelector('.offcanvas-body .list-group li:last-child');
      if (totalItem) {
        totalItem.innerHTML = `<span class="fw-bold">Total</span><strong>R$ ${total.toFixed(2)}</strong>`;
      }
    }

    // Adicionando o evento de remoção para os botões de lixeira
    const deleteButtons = document.querySelectorAll('.delete-item');
    deleteButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        const productId = this.getAttribute('data-id');
        removeFromCart(productId);
      });
    });
  }

  // Função para remover item do carrinho
  function removeFromCart(productId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart = cart.filter(product => product.id !== productId);

    localStorage.setItem('cart', JSON.stringify(cart));

    updateCart();  // Atualiza a visualização do carrinho
  }

  // A primeira chamada de updateCart deve ser feita logo ao carregar a página para garantir que o carrinho
  // seja renderizado, mesmo que o localStorage já tenha um item.
  updateCart(); // Chamada para garantir que o carrinho seja renderizado corretamente após a primeira adição
});
