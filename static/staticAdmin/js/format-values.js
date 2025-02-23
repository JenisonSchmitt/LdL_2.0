document.addEventListener('DOMContentLoaded', function () {
    const valorInput = document.getElementById('valor');

    valorInput.addEventListener('input', function (event) {
        let valor = event.target.value.replace(/\D/g, '');
        valor = (parseInt(valor, 10) / 100).toFixed(2); 
        valor = valor.replace('.', ',');

        event.target.value = valor;
    });
});
