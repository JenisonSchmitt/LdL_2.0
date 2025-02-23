$(document).ready(function() {
    $("#add-product").click(function() {
        let newProdutoItem = $(".produto-item:first").clone();
        
        newProdutoItem.find("input").val('');
        
        $("#produtos-container").append(newProdutoItem);
    });

    $(document).on("keyup", ".produto", function() {
        let termo = $(this).val().trim();
        let sugestoes = $(this).closest(".produto-item").find(".sugestoesproduto");

        if (termo.length < 3) {
            sugestoes.hide();
            return;
        }

        $.ajax({
            url: "/buscar-produtos-admin",
            method: "POST",
            data: { q: termo },
            success: function(response) {
                sugestoes.empty();

                if (response.length > 0) {
                    let select = $('<select class="sugestao-select"></select>');
                    select.append('<option disabled selected>Selecione um produto</option>');

                    response.forEach(produto => {
                        select.append(`<option value="${produto.id}" data-valor="${produto.valor}">${produto.nome}</option>`);
                    });

                    sugestoes.append(select);
                    sugestoes.show();
                } else {
                    sugestoes.append('<div class="mensagem-vazia">Nenhum produto encontrado</div>');
                    sugestoes.show();
                }
            }
        });
    });

    $(document).on("change", ".sugestao-select", function() {
        let nomeProduto = $(this).find("option:selected").text();
        let produtoId = $(this).find("option:selected").val(); 
        let produtoValor = $(this).find("option:selected").data("valor"); 
    
        $(this).closest(".produto-item").find(".produto").val(nomeProduto);
        $(this).closest(".produto-item").find(".produto_id").val(produtoId);
        $(this).closest(".produto-item").find(".produto_valor").val(produtoValor);
        $(this).closest(".produto-item").find(".sugestoesproduto").hide();
    });

    $(document).click(function(e) {
        if (!$(e.target).closest(".sugestoesproduto, .produto").length) {
            $(".sugestoesproduto").hide();
        }
    });
});
