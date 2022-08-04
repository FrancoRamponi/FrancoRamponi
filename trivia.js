const clave = "26 de abril";

function Verificador(){
    const inputFecha = document.getElementById("Fecha");
    const FechaValue = inputFecha.value;

    if (FechaValue == clave){
        const result = document.getElementById("Result");
        result.innerText = "♡♡♡ MUY BIEN RUBIECITA LINDA TE AMO MUCHÍSIMO ♡♡♡ \n ♡♡♡ SIEMPRE TE VOY A ESPERAR Y AYUDAR EN TODO ♡♡♡ \n ¿NOS COMPRAMOS ESAS PULSERAS? ";
    }
    else{
        const result = document.getElementById("Result");
        result.innerText = "Volvé a intentar, dale que vos sabés.";
    }


}

