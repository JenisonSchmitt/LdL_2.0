document.addEventListener("DOMContentLoaded", () => {
  const imagens = document.querySelectorAll("img[data-src]");
  imagens.forEach(img => {
    img.src = img.dataset.src;
  });
});
