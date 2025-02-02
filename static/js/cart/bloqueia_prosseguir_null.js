function verificarTotal() {
    const totalElement = document.getElementById('cart-total');
    const botaoProsseguir = document.getElementById('prosseguir-compra');
    const total = parseFloat(totalElement.textContent.replace('R$ ', '').replace(',', '.'));

    if (total === 0 || isNaN(total)) {
        botaoProsseguir.disabled = true;
    } else {
        botaoProsseguir.disabled = false;
    }
}

document.addEventListener('DOMContentLoaded', verificarTotal);

const observer = new MutationObserver(verificarTotal);
const totalElement = document.getElementById('cart-total');
if (totalElement) {
    observer.observe(totalElement, {
        childList: true, 
        subtree: true,
        characterData: true 
    });
}
