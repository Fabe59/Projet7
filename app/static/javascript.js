let form =document.querySelector("#request-input-form");
const spinner = document.getElementById("spinner");

/** 
 * function to create a class for the spinner div and display the spinner
*/
function showSpinner() {
    spinner.className = "show";
    setTimeout(() => {
    spinner.className = spinner.className.replace("show", "");
    }, 5000);
};

/** 
 * function to hide the spinner 
*/
function hideSpinner() {
    spinner.className = spinner.className.replace("show", "");
};

/** 
 * function to create a div to display the search reminder
*/
function grandPyAnswer(question) {
    let newDivAnswer = document.createElement('div');
    newDivAnswer.classList.add('answer');
    newDivAnswer.textContent = question;
    let parentNode = document.getElementById('response');
    parentNode.appendChild(newDivAnswer);
};

/** 
 * function to create a div to display the GrandPy message
*/
function grandpymessage(message) {
    let newDivMessage = document.createElement('div');
    newDivMessage.classList.add('grandpymessage');
    newDivMessage.textContent = message;
    let parentNode = document.getElementById('response')
    parentNode.appendChild(newDivMessage);
};

/** 
 * function to create a div to display answers
*/
function createResponse(text){
    let newDiv = document.createElement('div');
    newDiv.classList.add('response-display');
    newDiv.textContent = text;
    let parentNode = document.getElementById('response')
    parentNode.appendChild(newDiv);
};

/** 
 * function to create a div to display the url
*/
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

/** 
 * function to create a div to display the google map
*/
function createMap(lat, long) {
    // Creation of a div tag to display the map
    let newDivMap = document.createElement('div');
    newDivMap.classList.add('map-response');

    // Creation of a variable for coordinates
    let LatLng = {'lat': lat, 'lng': long};

    // Display the map in the created div, at the requested coordinates
    let map = new google.maps.Map(newDivMap, {
        zoom: 13,
        center: LatLng
        });

    // Display of the marker on the map at the desired coordinates
    let marker = new google.maps.Marker({
        position: LatLng,
        map: map,
        title: "Ta recherche t'amène ici"
        });

    // adding the new node to the parent node "response" to display everything
    let parentNode = document.getElementById("response");
    parentNode.appendChild(newDivMap);                  
};

/** 
 * function to create a "hr" tag
*/
function createhr() {
    let newHr = document.createElement('hr');
    newHr.classList.add('hr-response');
    let parentNode = document.getElementById("response");
    parentNode.appendChild(newHr);
    newHr.scrollIntoView({behavior: "smooth", block: "end"}); 
};

form.addEventListener("submit", function (event){
    event.preventDefault();

    showSpinner()
                        
    // Send the content of the form to the server
    fetch("/ajax", {
        method: "POST",
        body: new FormData(form)
    })
    // Returns a promise in JSON
    .then(function(response) {
        return response.json()
    })  
    //Display of the conversion of JSON into object in the console
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