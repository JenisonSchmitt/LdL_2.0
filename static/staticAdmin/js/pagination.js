    document.addEventListener("DOMContentLoaded", function () {
        const tabela = document.getElementById("tabela-produtos");
        const linhas = tabela.getElementsByTagName("tbody")[0].getElementsByTagName("tr");
        const btnAnterior = document.getElementById("btn-anterior");
        const btnProximo = document.getElementById("btn-proximo");
        const paginaAtualSpan = document.getElementById("pagina-atual");

        const itensPorPagina = 10; // Número de itens por página
        let paginaAtual = 1;

        // Função para exibir as linhas da página atual
        function exibirPagina(pagina) {
            const inicio = (pagina - 1) * itensPorPagina;
            const fim = inicio + itensPorPagina;

            for (let i = 0; i < linhas.length; i++) {
                if (i >= inicio && i < fim) {
                    linhas[i].style.display = "";
                } else {
                    linhas[i].style.display = "none";
                }
            }

            paginaAtualSpan.textContent = pagina;

            btnAnterior.disabled = pagina === 1;
            btnProximo.disabled = fim >= linhas.length;
        }

        btnAnterior.addEventListener("click", function () {
            if (paginaAtual > 1) {
                paginaAtual--;
                exibirPagina(paginaAtual);
                document.getElementById("top").scrollIntoView({ behavior: "smooth" });
            }
        });

        btnProximo.addEventListener("click", function () {
            if (paginaAtual < Math.ceil(linhas.length / itensPorPagina)) {
                paginaAtual++;
                exibirPagina(paginaAtual);
                document.getElementById("top").scrollIntoView({ behavior: "smooth" });
            }
        });

        exibirPagina(paginaAtual);
    });
