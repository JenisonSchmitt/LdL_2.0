document.addEventListener('DOMContentLoaded', function() {
    const quantityInputs = document.querySelectorAll('.quantity-input');

    quantityInputs.forEach(input => {
        input.addEventListener('input', function() {
            const productId = input.dataset.id;
            const newQuantity = parseInt(input.value) || 1;

            const hiddenQuantityInput = document.querySelector(`input[name="quantidade_${productId}"]`);
            if (hiddenQuantityInput) {
                hiddenQuantityInput.value = newQuantity;
            }

            const price = Number(input.closest('tr').querySelector('.cart-align-itens-price').textContent.replace('R$ ', '').replace(',', '.'));
            
            const totalPrice = (price * newQuantity).toFixed(2);

            const hiddenTotalInput = document.querySelector(`input[name="valor_total_${productId}"]`);
            if (hiddenTotalInput) {
                hiddenTotalInput.value = totalPrice.replace('.', ',');
            }

            const totalPriceElement = input.closest('tr').querySelector('.total-price strong');
            totalPriceElement.textContent = `R$ ${totalPrice.replace('.', ',')}`;

            updateCartTotal();
        });
    });

    function updateCartTotal() {
        let total = 0;
        const rows = document.querySelectorAll('tbody tr');

        rows.forEach(row => {
            const rowTotal = Number(row.querySelector('.total-price strong').textContent.replace('R$ ', '').replace(',', '.'));
            total += rowTotal;
        });

        document.getElementById('cart-total').textContent = total.toFixed(2).replace('.', ',');
    }

    updateCartTotal();
});