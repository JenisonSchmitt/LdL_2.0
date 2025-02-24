document.getElementById('cep').addEventListener('blur', function () {
    var cep = this.value.replace(/\D/g, ''); 

    if (cep !== "") {
        var validacep = /^[0-9]{8}$/; 

        if (validacep.test(cep)) {

            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    if (!data.erro) {
                        document.getElementById('rua').value = data.logradouro;
                        document.getElementById('cidade').value = data.localidade;
                        document.getElementById('estado').value = data.uf;
                    } else {
                        alert('CEP não encontrado.');
                    }
                })
                .catch(error => {
                    alert('Erro ao buscar o CEP.');
                    console.error('Erro:', error);
                });
        } else {
            alert('CEP inválido.');
        }
    }
});
