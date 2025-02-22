document.addEventListener('DOMContentLoaded', function() {
    const favoriteButtons = document.querySelectorAll('.btn-wishlist');

    favoriteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-id'); 

            fetch('/adicionar_favorito', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ product_id: productId }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById('popup_favorite_product').style.display = 'block';
                } else {
                    const errorMessage = data.message || 'Não foi possível adicionar o produto aos favoritos!';
                    document.getElementById('popup_favorite_product_erro').style.display = 'block';
                    document.querySelector('#popup_favorite_product_erro .modal-body p').textContent = errorMessage;
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                document.getElementById('popup_favorite_product_erro').style.display = 'block';
                document.querySelector('#popup_favorite_product_erro .modal-body p').textContent = 'Erro ao processar a requisição. Tente novamente mais tarde.';
            });
        });
    });

    document.getElementById('close-popup-success').addEventListener('click', function() {
        document.getElementById('popup_favorite_product').style.display = 'none';
    });

    document.getElementById('close-popup-error').addEventListener('click', function() {
        document.getElementById('popup_favorite_product_erro').style.display = 'none';
    });
});
