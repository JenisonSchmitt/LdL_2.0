document.addEventListener('DOMContentLoaded', function () {
    const swiper = new Swiper('.main-swiper-slider', {
        loop: true,
        navigation: {
            nextEl: '.carousel-control-next',
            prevEl: '.carousel-control-prev',
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
    });
    
    function next_slider_aut() {
        setInterval(() => {
            swiper.slideNext();
        }, 3000);
    }

    function stop_next_prev(){

    }

    next_slider_aut();
});
