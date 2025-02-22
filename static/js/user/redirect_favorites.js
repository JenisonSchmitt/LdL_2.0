function RedirectFavorites() {
    document.getElementById("products").scrollIntoView({ behavior: "smooth" });

    setTimeout(function() {
        window.location.href = '/products-favorite#products';  
    }, 5000); 
}

window.onload = RedirectFavorites;
