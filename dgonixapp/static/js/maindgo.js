function validar(){
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var correo = document.getElementById("correo").value;
    var celular = document.getElementById("celular").value;
    var rut = document.getElementById("rut").value;
    var password = document.getElementById("contrasena").value;

    if(nombre === ""){
        $("#mensaje1").text("Campo nombre no puede estar vacío")
    }

    if(apellido === ""){
        $("#mensaje2").text("Campo apellido no puede estar vacío ");
    }

    if(correo === ""){
        $("#mensaje3").text("Campo correo no puede estar vacío ");
    } else if (!validarcorreo(correo)){
        $("#mensaje3").text("El correo debe contener '@'")
    }

    if(celular === ""){
        $("#mensaje4").text("Campo celular no puede estar vacío ");
    }

    if(rut === ""){
        $("#mensaje5").text("Campo rut no puede estar vacío ");
    }

    if(password === ""){
        $("#mensaje6").text("Campo contraseña no puede estar vacío ");

    }
}

function validarcorreo(correo){
    return correo.includes("@");
}



//Funcion api google maps
const dgoCoords = { lat: -33.01008605957031, lng: -71.54591369628906 };
let map;

function initMap() {
    const mapDiv = document.getElementById("map");
    map = new google.maps.Map(mapDiv, {
        center: dgoCoords,
        zoom: 18,
    });
    const marker = new google.maps.Marker({
        position: dgoCoords,
        map: map,
    });
}
/*const dgoCoords = { lat: -33.01008605957031, lng: -71.54591369628906};
const mapDiv= document.getElementById("map");
let map;
function initMap(){
    map = new google.maps.Map(mapDiv, {
        center:dgoCoords,
        zoom: 18,
    })
    marker= new google.maps.Marker({
        position: dgoCoords,
        map: map,
    });
}*/


function validarFormulario() {
    var email = document.getElementById("InputEmail1").value;
    var password = document.getElementById("InputPassword1").value;
    


    if (email == "") {
        document.getElementById("mensajecorreo").innerHTML = "Campo correo no puede estar vacío";
        return false;
    } else {
        document.getElementById("mensajecorreo").innerHTML = "";
    }

}

//Api de productos y LocalStorage
function populatedCategories(categories) {
    console.log('Categorías:', categories);
}

var storedCategories = localStorage.getItem('category');

if (storedCategories) {

    populatedCategories(JSON.parse(storedCategories));
} else {
    fetch('https://fakestoreapi.com/products?limit=7')
        .then(response => response.json())
        .then(data => {
        
            localStorage.setItem('category', JSON.stringify(data));
        
            populatedCategories(data);
        })
        .catch(error => console.error('Error fetching data:', error));
}
