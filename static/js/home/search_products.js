function searchProducts() {
  const query = document.getElementById("search-input").value;

  if (query.length >= 3) { 
    fetch(`/search_products?q=${query}`)
      .then(response => response.json())
      .then(data => {
        displayResults(data);
      })
      .catch(error => console.error("Erro ao buscar produtos:", error));
  } else {
    const resultsDiv = document.getElementById("search-results");
    resultsDiv.innerHTML = "";
    resultsDiv.style.display = "none"; 
  }
}

function displayResults(data) {
  const resultsDiv = document.getElementById("search-results");
  resultsDiv.innerHTML = ""; 

  resultsDiv.style.position = "absolute";
  resultsDiv.style.top = "100px";
  resultsDiv.style.left = "47%";
  resultsDiv.style.transform = "translateX(-50%)";
  resultsDiv.style.zIndex = "9999";
  resultsDiv.style.backgroundColor = "#fafafa";
  resultsDiv.style.borderRadius = "10px";
  resultsDiv.style.padding = "10px";
  resultsDiv.style.boxShadow = "0 4px 10px rgba(0, 0, 0, 0.1)";
  resultsDiv.style.display = "block"; 

  if (data.length === 0) {
    resultsDiv.innerHTML = "<p>Nenhum produto encontrado.</p>";
    return;
  }

  data.forEach(product => {
    const itemDiv = document.createElement("div");
    itemDiv.classList.add("item", product.tipo_produto, "col-md-4", "col-lg-3", "my-4");

    const imagePath = product.tipo_produto === "Maquiagem" ?
      `../static/images/maquiagem/${product.nome.toLowerCase().replace(/ /g, '')}.png` :
      `../static/images/skincare/${product.nome.toLowerCase().replace(/ /g, '')}.png`;

    itemDiv.innerHTML = `
      <div class="product-card-search_products">
        <a href="/produtos/${product.id}#produto" class="product-link-search_products">
          <img src="${imagePath}" class="img-fluid rounded-4" alt="image" style="width: 50px; height: 50px; object-fit: cover; margin-right: 10px;">
          <div class="product-info-search_products">
            <h3 class="card-title m-0" style="font-size: 16px; font-weight: normal; line-height: 1.2;">${product.nome}</h3>
          </div>
          <h3 class="secondary-font text-primary" style="margin-left: auto; font-size: 14px; font-weight: normal; line-height: 1.2;">R$ ${product.valor}</h3>
        </a>
      </div>
    `;

    resultsDiv.appendChild(itemDiv);
  });
}




// Função de busca para mobile
function searchProductsMobile() {
  const query = document.getElementById("search-input-mobile").value;

  if (query.length >= 3) {
    fetch(`/search_products?q=${query}`)
      .then(response => response.json())
      .then(data => {
        displayResultsMobile(data);
      })
      .catch(error => console.error("Erro ao buscar produtos:", error));
  } else {
    const resultsDiv = document.getElementById("search-results-mobile");
    resultsDiv.innerHTML = "";
    resultsDiv.style.display = "none";
  }
}

// Função para exibir os resultados no mobile
function displayResultsMobile(data) {
  const resultsDiv = document.getElementById("search-results-mobile");
  resultsDiv.innerHTML = "";

  resultsDiv.style.backgroundColor = "#fafafa";
  resultsDiv.style.borderRadius = "10px";
  resultsDiv.style.padding = "10px";
  resultsDiv.style.boxShadow = "0 4px 10px rgba(0, 0, 0, 0.1)";
  resultsDiv.style.display = "block";

  if (data.length === 0) {
    resultsDiv.innerHTML = "<p>Nenhum produto encontrado.</p>";
    return;
  }

  data.forEach(product => {
    const itemDiv = document.createElement("div");
    itemDiv.classList.add("item", product.tipo_produto, "my-3");

    const imagePath = product.tipo_produto === "Maquiagem" ?
      `../static/images/maquiagem/${product.nome.toLowerCase().replace(/ /g, '')}.png` :
      `../static/images/skincare/${product.nome.toLowerCase().replace(/ /g, '')}.png`;

    itemDiv.innerHTML = `
      <div class="product-card-search_products">
        <a href="/produtos/${product.id}#produto" class="product-link-search_products d-flex align-items-center">
          <img src="${imagePath}" class="img-fluid rounded-4" alt="image" style="width: 50px; height: 50px; object-fit: cover; margin-right: 10px;">
          <div class="product-info-search_products flex-grow-1">
            <h3 class="card-title m-0" style="font-size: 16px; font-weight: normal; line-height: 1.2;">${product.nome}</h3>
          </div>
          <h3 class="secondary-font text-primary" style="font-size: 14px; font-weight: normal; line-height: 1.2;">R$ ${product.valor}</h3>
        </a>
      </div>
    `;

    resultsDiv.appendChild(itemDiv);
  });
}