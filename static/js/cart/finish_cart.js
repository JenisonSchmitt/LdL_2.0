document.addEventListener('DOMContentLoaded', function() {
    const finishButton = document.querySelector('.btn.btn-primary.btn-lg');
    if (finishButton) {
      finishButton.addEventListener('click', function() {
        const cart = JSON.parse(localStorage.getItem('cart')) || [];
  
        if (cart.length === 0) {
          alert('Seu carrinho está vazio!');
        } else {
          console.log('Finalizando pedido com os itens:', cart);
          // Aqui você pode enviar os dados do carrinho para um backend ou processar o pagamento
        }
      });
    } else {
      console.log("Botão de finalizar pedido não encontrado.");
    }
  });
  