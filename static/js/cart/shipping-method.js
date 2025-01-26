document.addEventListener('DOMContentLoaded', function() {
    let totalCartValue = localStorage.getItem('totalCartValue') || '0.00';
    document.getElementById('cart-total').textContent = formatCurrency(totalCartValue);

    document.getElementById('cep').addEventListener('input', function() {
        let cep = this.value.replace(/\D/g, '');  
        if (cep.length > 5) {
            cep = cep.replace(/(\d{5})(\d)/, '$1-$2');
        }
        this.value = cep;
        document.getElementById('shipping-options').removeAttribute('disabled');
    });

    document.getElementById('shipping-options').addEventListener('change', function() {
        let shippingValue = parseFloat(this.value) || 0;
        document.getElementById('shipping-value').textContent = formatCurrency(shippingValue);

        let finalTotal = parseFloat(totalCartValue) + shippingValue;
        document.getElementById('final-total').textContent = formatCurrency(finalTotal);
    });
});

function formatCurrency(value) {
    return `R$ ${(isNaN(parseFloat(value)) ? '0,00' : parseFloat(value).toFixed(2).replace('.', ','))}`;
}

document.getElementById('cep-btn').addEventListener('click', function() {
    const cep = document.getElementById('cep').value;
});

document.getElementById('cep').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        const cep = document.getElementById('cep').value;
    }
});

document.getElementById('cep').addEventListener('blur', function() {
    const cep = this.value.replace(/\D/g, '');  
    if (cep.length === 8) {  
        fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(response => response.json())
            .then(data => {
                if (!data.erro) {
                    document.getElementById('shipping-info').innerHTML = `
                        <p class="color-pink"><strong>Rua:</strong> ${data.logradouro}</p>
                        <p class="color-pink"><strong>Bairro:</strong> ${data.bairro}</p>
                        <p class="color-pink"><strong>Cidade:</strong> ${data.localidade}</p>
                        <p class="color-pink"><strong>Estado:</strong> ${data.uf}</p>
                    `;

                    showShippingFields(true);
                    document.getElementById('shipping-options').disabled = false;
                } else {
                    document.getElementById('shipping-info').innerHTML = `
                        <p class="color-purple">CEP não encontrado. Verifique o número do CEP.</p>
                    `;
                    showShippingFields(false);
                    document.getElementById('shipping-options').disabled = true;
                }
            })
            .catch(error => {
                document.getElementById('shipping-info').innerHTML = `
                    <p class="color-purple">Erro ao consultar o CEP. Tente novamente mais tarde.</p>
                `;
                showShippingFields(false);
                document.getElementById('shipping-options').disabled = true;
            });
    } else {
        document.getElementById('shipping-info').innerHTML = `
        <p class="color-purple">CEP inválido. Verifique se há 8 dígitos no CEP.</p>
        `;
        showShippingFields(false);
        document.getElementById('shipping-options').disabled = true;
    }
});

function showShippingFields(show) {
    const displayStyle = show ? 'block' : 'none';
    document.getElementById('numero').style.display = displayStyle;
    document.getElementById('complemento').style.display = displayStyle;
    document.getElementById('shipping-options').style.display = displayStyle;
    document.getElementById('numero-label').style.display = displayStyle;
    document.getElementById('complemento-label').style.display = displayStyle;
    document.getElementById('shipping-options-label').style.display = displayStyle;
}


document.addEventListener('DOMContentLoaded', function() {
    function checkFormCompletion() {
        const cep = document.getElementById('cep').value.trim();
        const numero = document.getElementById('numero').value.trim();
        const complemento = document.getElementById('complemento').value.trim();
        const shippingOption = document.getElementById('shipping-options').value !== 'Selecione a forma de envio';

        const isFormValid = cep.length === 9 && numero !== '' && complemento !== '' && shippingOption;

        // Habilita ou desabilita o botão 'Prosseguir'
        document.getElementById('btn-prosseguir').disabled = !isFormValid;
    }

    // Verifica o formulário a cada alteração
    document.getElementById('cep').addEventListener('input', checkFormCompletion);
    document.getElementById('numero').addEventListener('input', checkFormCompletion);
    document.getElementById('complemento').addEventListener('input', checkFormCompletion);
    document.getElementById('shipping-options').addEventListener('change', checkFormCompletion);

    checkFormCompletion();  // Verifica ao carregar a página
});