function showSection(targetId) {
    document.querySelectorAll('.container-fluid-dados').forEach(section => {
        section.style.display = 'none';
    });

    const targetSection = document.getElementById(targetId);
    if (targetSection) {
        targetSection.style.display = 'block';
    }
}

document.querySelectorAll('.tm-nav-link').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault(); 
        const target = this.getAttribute('data-target'); 
        showSection(target); 
    });
});

document.addEventListener('DOMContentLoaded', function () {
    showSection('estatisticas'); 
});