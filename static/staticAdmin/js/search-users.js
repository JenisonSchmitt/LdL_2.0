$(document).ready(function() {
    $("#cliente").on("keyup", function() {
        let termo = $(this).val().trim();
        let sugestoes = $("#sugestoescliente");

        if (termo.length < 3) {
            sugestoes.hide();
            return;
        }

        $.ajax({
            url: "/buscar-clientes-admin",
            method: "POST",
            data: { q: termo },
            success: function(response) {
                sugestoes.empty();

                if (response.length > 0) {
                    let select = $('<select class="sugestao-select-cliente"></select>');
                    select.append('<option disabled selected>Selecione um Cliente</option>');

                    response.forEach(cliente => {
                        let option = `<option 
                            value="${cliente.id}" 
                        >${cliente.nome}</option>`;
                        
                        select.append(option);
                    });

                    sugestoes.append(select);
                    sugestoes.show();
                } else {
                    sugestoes.append('<div class="mensagem-vazia-cliente">Nenhum cliente encontrado</div>');
                    sugestoes.show();
                }
            }
        });
    });

    $(document).on("change", ".sugestao-select-cliente", function() {
        let selected = $(this).find("option:selected");
        let nomecliente = selected.text();
        let clienteId = selected.val();
        
        $("#cliente").val(nomecliente);
        $("#cliente_id").val(clienteId);
        
        $("#sugestoescliente").hide();
    });

    $(document).click(function(e) {
        if (!$(e.target).closest("#sugestoescliente, #cliente").length) {
            $("#sugestoescliente").hide();
        }
    });
});
