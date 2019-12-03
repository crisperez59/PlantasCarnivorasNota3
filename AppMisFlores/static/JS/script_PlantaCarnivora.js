$("#formulario1").validate({
    rules: {
        "txtCorreoElectronico": {
            required: true,
            email: true
        },

        "txtNombreCompleto": {
            required: true,
            lettersonly: true
        },

        "txtFechaNacimiento":{
            required: true,
            max: "2000-12-31"
            
        },

        "txtTelefono":{
            required: true,
            digits: true
        },

        "cmbTipoVivienda":{
            required: true,
        }

        
    }, //--->fin de reglas
    messages: {
        "txtEmail": {
            required: "te falto el email ",
            email: "No tiene el formato email"
        },
        "txtNombreCompleto": {
            required: "Te falto el nombre ",
            lettersonly: "Solo se deben ingresar letras"
        },
        
        "txtFechaNacimiento": {
            required: "Falta fecha de nacimiento",
            max: "El año debe ser menor a 2001"
        },

        "txtTelefono":{
            required: "Debe Ingresar el numero",
            digits: "El numero solo debe tener numeros"
        },
        
        "cmbTipoVivienda":{
            required: "Debe ingresar un tipo de vivienda"

        }

    } //Fin mensajes
}//final del obejto
);