document.addEventListener("DOMContentLoaded", function() {
    const produtosContainer = document.getElementById('produtos');
    const produtosItems = produtosContainer.getElementsByClassName('produto-item');
    const itemHeight = produtosItems[0].offsetHeight + 70; // Altura de um item de produto
    const numItems = produtosItems.length;
    const minHeight = itemHeight * numItems;

    produtosContainer.style.minHeight = `${minHeight}px`;
});