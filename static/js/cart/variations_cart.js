document.addEventListener("DOMContentLoaded", function() {
    const selects = document.querySelectorAll('select');
    const btnCarrinho = document.getElementById('btn-carrinho');
    const popup = document.getElementById('popup');
    const closePopupButton = document.getElementById('close-popup');
    const carrinhoVariacao = document.getElementById('carrinhoVariacao');

    function checkSelectValue() {
        let valid = false;
        
        selects.forEach(select => {
            const value = select.value;
            if (value && value !== "0") {
                valid = true; 
            }
        });

        if (valid) {
            carrinhoVariacao.style.display = "flex";  
        } else {
            carrinhoVariacao.style.display = "none"; 
        }
    }

    popup.style.display = "flex";
    carrinhoVariacao.style.display = "none"; 

    closePopupButton.addEventListener("click", function() {
        popup.style.display = "none";
    });

    checkSelectValue();

    selects.forEach(select => {
        select.addEventListener("change", checkSelectValue);
    });
});


function updateProductNameAndId(produtoId, selectElement) {
    // Pega o valor da variação selecionada (Nome-ID)
    const variacaoSelecionada = selectElement.value;

    // Se uma variação for selecionada, separa o Nome e o ID (considerando que a estrutura é: nome-ID)
    if (variacaoSelecionada) {
        const [variacaoId, variacaoNome] = variacaoSelecionada.split('-');
        
        // Atualiza o data-id do botão "Adicionar ao Carrinho" com o ID da variação
        const btnCart = document.querySelector(`#addToCart-${produtoId}`);
        if (btnCart) {
            // Atualiza o data-id com o ID da variação
            btnCart.setAttribute('data-id', variacaoId);

            // Atualiza o data-name com o nome do produto + nome da variação
            const nomeProdutoComVariacao = document.querySelector(`#addToCart-${produtoId}`).getAttribute('data-name') + ' ' + variacaoNome;
            btnCart.setAttribute('data-name', nomeProdutoComVariacao);
        }
    }
}