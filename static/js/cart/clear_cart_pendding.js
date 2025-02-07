function clearCart() {
    document.getElementById("info").scrollIntoView({ behavior: "smooth" });

    localStorage.removeItem('cart');

    if (typeof updateCart === 'function') {
        updateCart(); 
    }

    setTimeout(function() {
        window.location.href = '/pedidos#requested';  
    }, 7000); 
}

window.onload = clearCart;
