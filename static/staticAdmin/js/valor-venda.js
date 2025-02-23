$(document).ready(function() {
    function calcularValorTotal() {
        let valorTotal = 0;

        $(".produto-item").each(function() {
            let quantidade = parseFloat($(this).find(".qtdproduto").val()) || 0;
            let valorProduto = parseFloat($(this).find(".produto_valor").val()) || 0;
            valorTotal += quantidade * valorProduto;
        });

        let valorFrete = parseFloat($("#valor").val()) || 0;
        valorTotal += valorFrete;

        let formaPagamento = $("#forma_pgt").val();

        if (formaPagamento === "bank_transfer") {
            valorTotal *= 0.95;
        }

        $("#valor_total").val(valorTotal.toFixed(2));
    }

    $(document).on("change", ".sugestao-select", function() {
        let produtoValor = $(this).find("option:selected").data("valor");
        $(this).closest(".produto-item").find(".produto_valor").val(produtoValor);
        calcularValorTotal();
    });

    $(document).on("input", ".qtdproduto", function() {
        calcularValorTotal();
    });

    $(document).on("input", "#valor", function() {
        calcularValorTotal();
    });

    $(document).on("change", "#forma_pgt", function() {
        calcularValorTotal();
    });
});