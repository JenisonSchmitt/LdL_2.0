document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.btn-avise').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault(); 
            const productId = button.getAttribute('data-id'); 
            window.location.href = `/avise/${productId}`; 
        });
    });
});
