function validarFormulario() {
    const senha = document.getElementById('senha').value;
    const confirmeSenha = document.getElementById('confirme-senha').value;
    
    if (senha !== confirmeSenha) {
        alert('As senhas não coincidem!');
        return false;
    }
    return true;
}

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('cpf').addEventListener('input', function (e) {
        let cpf = e.target.value.replace(/\D/g, ''); // Remove caracteres não numéricos
        if (cpf.length > 11) cpf = cpf.substring(0, 11);
        e.target.value = cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
    });

    document.getElementById('telefone').addEventListener('input', function (e) {
        let telefone = e.target.value.replace(/\D/g, ''); // Remove caracteres não numéricos
        if (telefone.length > 11) telefone = telefone.substring(0, 11);
        if (telefone.length === 11) {
            e.target.value = telefone.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
        } else {
            e.target.value = telefone.replace(/(\d{2})(\d{4})(\d{0,4})/, '($1) $2-$3');
        }
    });

    document.getElementById('cep').addEventListener('input', function (e) {
        let cep = e.target.value.replace(/\D/g, ''); // Remove caracteres não numéricos
        if (cep.length > 8) cep = cep.substring(0, 8);
        e.target.value = cep.replace(/(\d{5})(\d{3})/, '$1-$2');
    });
});
