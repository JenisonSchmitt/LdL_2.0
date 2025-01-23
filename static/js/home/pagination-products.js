  var swiper = new Swiper('.products-carousel', {
    loop: false,             // Permite looping contínuo
    autoplay: {
      delay: 5000,
      disableOnInteraction: false, 
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });
