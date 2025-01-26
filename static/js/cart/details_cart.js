document.addEventListener('DOMContentLoaded', function() {
    function updateCartTotal() {
        let total = 0;
        document.querySelectorAll('.total-price').forEach(function(el) {
            total += parseFloat(el.textContent.replace('R$ ', '').replace(',', '.'));
        });
        document.getElementById('cart-total').textContent = total.toFixed(2).replace('.', ',');
    }

    document.querySelectorAll('.quantity-input').forEach(function(input) {
        input.addEventListener('change', function() {
            let quantity = parseInt(this.value);
            let price = parseFloat(this.closest('tr').querySelector('.total-price').getAttribute('data-price'));
            let totalElement = this.closest('tr').querySelector('.total-price');

            totalElement.textContent = `R$ ${(quantity * price).toFixed(2).replace('.', ',')}`;
            updateCartTotal();
        });
    });

    document.querySelectorAll('.remove-item').forEach(function(button) {
        button.addEventListener('click', function() {
            let productId = this.getAttribute('data-id');
            let row = this.closest('tr');

            let cart = JSON.parse(localStorage.getItem('cart')) || [];
            cart = cart.filter(item => item.id !== productId);
            localStorage.setItem('cart', JSON.stringify(cart));

            row.remove();
            updateCartTotal();

            const successCartClearModal = new bootstrap.Modal(document.getElementById('successCartClearModal'));
            successCartClearModal.show();

        });
    });
    document.querySelector('.btn-primary.px-4.pt-3.pb-3').addEventListener('click', function(event) {
        let cartItems = [];

        document.querySelectorAll('tbody tr').forEach(function(row) {
            let productId = row.querySelector('.quantity-input').getAttribute('data-id');
            let quantity = row.querySelector('.quantity-input').value;
            let total = row.querySelector('.total-price').textContent.replace('R$ ', '').replace(',', '.');

            cartItems.push({
                id: productId,
                quantity: quantity,
                total: parseFloat(total).toFixed(2)
            });
        });

        localStorage.setItem('cartData', JSON.stringify(cartItems));

        let totalCartValue = document.getElementById('cart-total').textContent.replace(',', '.');
        localStorage.setItem('totalCartValue', totalCartValue);

        console.log('Dados do carrinho salvos:', cartItems, 'Total:', totalCartValue);
    });

    updateCartTotal();
});