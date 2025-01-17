document.addEventListener('DOMContentLoaded', function() {
    const categorySelect = document.getElementById('categorySelect');
    if (categorySelect) {
      categorySelect.addEventListener('change', function() {
        const selectedValue = this.value;
        if (selectedValue) {
          window.location.href = selectedValue;
        }
      });
    }
  });
  