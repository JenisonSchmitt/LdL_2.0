document.addEventListener('DOMContentLoaded', function() {
    const cepInput = document.getElementById('cep');
    const shippingSelect = document.getElementById('shipping-options');
    const shippingValueInput = document.getElementById('shipping-value-input');
    const finalTotalInput = document.getElementById('final-total-input');
    const cartTotalElement = document.getElementById('cart-total');
    const shippingValueElement = document.getElementById('shipping-value');
    const finalTotalElement = document.getElementById('final-total');
    const btnProsseguir = document.getElementById('btn-prosseguir');

    function calcularValorFinal() {
        const cartTotal = parseFloat(cartTotalElement.textContent.replace('R$ ', '').replace(',', '.'));
        const shippingValue = parseFloat(shippingValueInput.value.replace(',', '.'));
        const finalTotal = cartTotal + shippingValue;

        finalTotalInput.value = finalTotal.toFixed(2);
        finalTotalElement.textContent = `R$ ${finalTotal.toFixed(2).replace('.', ',')}`;
    }

    shippingSelect.addEventListener('change', function() {
        const selectedOption = shippingSelect.options[shippingSelect.selectedIndex];
        const shippingPrice = selectedOption.value.replace(',', '.');

        shippingValueInput.value = shippingPrice;
        shippingValueElement.textContent = `R$ ${parseFloat(shippingPrice).toFixed(2).replace('.', ',')}`;

        calcularValorFinal();
        btnProsseguir.disabled = false; 
    });

    cepInput.addEventListener('input', function() {
        let cep = cepInput.value;

        // Verifica se o CEP tem exatamente 9 caracteres
        if (cep.length === 9) {
            if (!cep || cep === "undefined" || cep === null) {
                alert('Por favor, insira um CEP válido!');
                return;
            }


            fetch('/calculate_shipping', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ cep: cep })
            })
            .then(response => {
                return response.json();
            })
            .then(data => {

                const shippingOptionsLabel = document.getElementById('shipping-options-label');

                if (data && data.length > 0) {
                    shippingSelect.innerHTML = '';

                    const fixedSelected = document.createElement('option');
                    const fixedOption = document.createElement('option');
                    fixedSelected.textContent = "Selecione a forma de envio";
                    fixedSelected.selected = true;
                    fixedSelected.disabled = true;
                    shippingSelect.appendChild(fixedSelected);

                    data.forEach(option => {
                        const optionElementWithImage = document.createElement('option');
                        optionElementWithImage.value = option.price.replace('.', ',');
                        optionElementWithImage.textContent = `${option.namecompany} - ${option.name} - R$ ${parseFloat(option.price).toFixed(2).replace('.', ',')}`;

                        if (option.custom_delivery_range) {
                            const minDays = option.custom_delivery_range.min;
                            const maxDays = option.custom_delivery_range.max;
                            optionElementWithImage.textContent += ` (Entre ${minDays} - ${maxDays} dias)`;
                        }

                        shippingSelect.appendChild(optionElementWithImage);
                    });

                    fixedOption.value = "0.00";
                    fixedOption.textContent = "Combinar retirada R$0,00 (Tubarão/SC - Centro)";
                    shippingSelect.appendChild(fixedOption);

                    shippingSelect.disabled = false;
                    shippingSelect.style.display = 'block';
                    shippingOptionsLabel.style.display = 'block';
                } else {
                    console.log('Erro ao calcular o frete:', data);
                    alert('Erro ao calcular o frete!');
                }
            })
            .catch(error => {
                console.log('Erro na requisição:', error);
                alert('Erro na requisição!');
            });
        }
    });
});

document.getElementById('shipping-options').addEventListener('change', function() {
    var selectedOptionText = this.options[this.selectedIndex].text;
    document.getElementById('forma_envio_text').value = selectedOptionText;
});