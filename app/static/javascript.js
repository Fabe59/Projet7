let form =document.querySelector("#request-input-form");
const spinner = document.getElementById("spinner");

function showSpinner() {
    spinner.className = "show";
    setTimeout(() => {
    spinner.className = spinner.className.replace("show", "");
    }, 5000);
};

function hideSpinner() {
    spinner.className = spinner.className.replace("show", "");
};

function grandPyAnswer(question) {
    let newDivAnswer = document.createElement('div');
    newDivAnswer.classList.add('answer');
    newDivAnswer.textContent = question;
    let parentNode = document.getElementById('response');
    parentNode.appendChild(newDivAnswer);
};

function grandpymessage(message) {
    let newDivMessage = document.createElement('div');
    newDivMessage.classList.add('grandpymessage');
    newDivMessage.textContent = message;
    let parentNode = document.getElementById('response')
    parentNode.appendChild(newDivMessage);
};

function createResponse(text){
    let newDiv = document.createElement('div');
    newDiv.classList.add('response-display');
    newDiv.textContent = text;
    let parentNode = document.getElementById('response')
    parentNode.appendChild(newDiv);
};

function createAResponse(url){
    let newA = document.createElement('a');
    newA.classList.add('response-url');
    newA.setAttribute('target', '_blank');
    let linkText = document.createTextNode("En savoir plus avec Wikipédia");
    newA.appendChild(linkText);
    newA.title = "Plus d'infos?";
    newA.href = url;
    let parentNode = document.getElementById("response");
    parentNode.appendChild(newA);
};

function createMap(lat, long) {
    //creation de la div pour afficher la map
    let newDivMap = document.createElement('div');
    newDivMap.classList.add('map-response');

    // création d'une variable pour les coordonnées
    let LatLng = {'lat': lat, 'lng': long};

    // appel de la carte dans la div crééé, au coordonnées demandées
    let map = new google.maps.Map(newDivMap, {
        zoom: 13,
        center: LatLng
        });

    // affichage du marqeur sur la carte précédente aux coordonnées voulues
    let marker = new google.maps.Marker({
        position: LatLng,
        map: map,
        title: "Ta recherche t'amène ici"
        });

    // ajout du nouveau noeud au noeud parent "response" pour afficher le tout
    let parentNode = document.getElementById("response");
    parentNode.appendChild(newDivMap);                    
};

function createhr() {
    let newHr = document.createElement('hr');
    newHr.classList.add('hr-response');
    let parentNode = document.getElementById("response");
    parentNode.appendChild(newHr);
};

form.addEventListener("submit", function (event){
    event.preventDefault();

    showSpinner()
                        
    // Envoyer le contenu du formulaire au serveur
    fetch("/ajax", {
        method: "POST",
        body: new FormData(form)
    })
    // retourne une promesse en JSON
    .then(function(response) {
        return response.json()
    })  
    //affichage de la conversion du JSON en objet dans la console
    .then(function(json) {
        hideSpinner()
        console.log(json)
    grandPyAnswer(json['question'])
    grandpymessage(json['message'])
    createResponse(json['address'])
    createResponse(json['info'])
    createAResponse(json['url'])
    createMap(json['latitude'], json['longitude'])
    createhr();
    })
    //.then(response => response.json())
    //.then(json => console.log(json))
});