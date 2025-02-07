document.getElementById("proceedPaymentBtn").addEventListener("click", function() {
    var paymentMethodModal = new bootstrap.Modal(document.getElementById("paymentMethodModal"));
    paymentMethodModal.show();
});

document.getElementById("pixButton").addEventListener("click", function() {
    const form = document.getElementById("formulariopagamento");  // Seleciona o formulário pelo id
    form.action = "/make-payment-pix";

    var paymentMethodModal = new bootstrap.Modal(document.getElementById("paymentMethodModal"));
    paymentMethodModal.hide();

    document.getElementById("submitPaymentBtn").click();
});

document.getElementById("creditCardButton").addEventListener("click", function() {
    const form = document.getElementById("formulariopagamento");  // Seleciona o formulário pelo id
    form.action = "/make-payment";

    var paymentMethodModal = new bootstrap.Modal(document.getElementById("paymentMethodModal"));
    paymentMethodModal.hide();

    document.getElementById("submitPaymentBtn").click();
});
