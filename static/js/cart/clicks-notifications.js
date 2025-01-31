function goToCart() {
  const modalElement = document.getElementById('successCartAddModal');
  if (modalElement) {
    modalElement.classList.remove('show');
    modalElement.setAttribute('aria-hidden', 'true');
    modalElement.style.display = 'none';
  }

  const backdrop = document.querySelector('.modal-backdrop');
  if (backdrop) {
    backdrop.remove();
  }

  document.body.classList.remove('modal-open');

  const offcanvasCart = document.getElementById('offcanvasCart');
  if (offcanvasCart) {
    const bsOffcanvas = new bootstrap.Offcanvas(offcanvasCart);
    bsOffcanvas.show();
  }
}

function afterclick() {
  const modalElement = document.getElementById('successCartAddModal');
  if (modalElement) {
    modalElement.classList.remove('show');
    modalElement.setAttribute('aria-hidden', 'true');
    modalElement.style.display = 'none';
  }

  const backdrop = document.querySelector('.modal-backdrop');
  if (backdrop) {
    backdrop.remove();
  }

  document.body.classList.remove('modal-open');
}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.btn-cart').forEach(function(button) {
    button.addEventListener('click', function(event) {
      event.preventDefault();
      const productId = this.getAttribute('data-id');
      showSuccessNotification();
    });
  });
});

function showSuccessNotification() {
  const successModal = document.getElementById('successCartAddModal');
  if (successModal) {
    successModal.classList.add('show');
    successModal.setAttribute('aria-hidden', 'false');
    successModal.style.display = 'block';
    document.body.classList.add('modal-open');
  }
}

function showItemDeletedNotification() {
  const successModal = document.getElementById('successCartDeleteModal');
  if (successModal) {
    successModal.classList.add('show');
    successModal.setAttribute('aria-hidden', 'false');
    successModal.style.display = 'block';
    document.body.classList.add('modal-open');
  }
}
