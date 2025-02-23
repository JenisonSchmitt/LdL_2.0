$(document).ready(function() {
    function toggleFreteFields() {
        const envio = $('#envio').val();
        
        if (envio === 'Envio') {
            $('#valor').closest('.form-group').show();

        } else {
            $('#valor').closest('.form-group').hide();

        }
    }

    toggleFreteFields();

    $('#envio').change(function() {
        toggleFreteFields();
    });
});
