// Mova as funções para o escopo global
function goToCart() {
  const successModal = new bootstrap.Modal(document.getElementById('successCartAddModal'));
  successModal.hide(); // Fecha o modal
  const offcanvasCart = document.getElementById('offcanvasCart');
  if (offcanvasCart) {
    const bsOffcanvas = new bootstrap.Offcanvas(offcanvasCart);
    bsOffcanvas.show();  // Exibe o carrinho
  }

  // Recarrega a página após o fechamento do modal
}

function afterclick() {
  const successModal = new bootstrap.Modal(document.getElementById('successCartAddModal'));

  // Fecha o modal
  successModal.hide();

  // Quando o modal for fechado, remove a sobrecarga (fundo cinza)
  successModal._element.addEventListener('hidden.bs.modal', function () {
    document.body.classList.remove('modal-open'); // Remove a classe 'modal-open'
    const backdrop = document.querySelector('.modal-backdrop');
    if (backdrop) {
      backdrop.remove(); // Remove o fundo cinza
    }
  });

  // Recarrega a página após o fechamento do modal
  location.reload();
}

// Função para adicionar produto ao carrinho
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.btn-cart').forEach(function(button) {
    button.addEventListener('click', function(event) {
      event.preventDefault();
      const productId = this.getAttribute('data-id');
      showSuccessNotification();  // Exibe a notificação de sucesso
    });
  });

  function showSuccessNotification() {
    const successModal = new bootstrap.Modal(document.getElementById('successCartAddModal'));
    successModal.show();  // Exibe o modal de sucesso
  }
});