var swiper = new Swiper('.products-carousel', {
  loop: false,  // Desativa o looping
  autoplay: {
    delay: 4000,  // A cada 5 segundos, troca o slide
    disableOnInteraction: false,  // Não desativa o autoplay ao interagir
  },
  slidesPerView: 'auto',  // Define a largura do slide como 'auto', baseada no CSS
  spaceBetween: 20,  // Não há espaço entre os slides
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});
