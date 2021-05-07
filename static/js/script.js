$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
});

$(document).ready(function () {
    $('input#input_text, textarea#location_description').characterCounter();
    $('input#input_text, textarea#location_name').characterCounter();
});


//This function will get the marker's current location and then add the lat/long
//values to our textfields so that we can save the location.
function markerLocation() {
    //Get location.
    var currentLocation = marker.getPosition();
    //Add lat and lng values to a field that we can save.
    document.getElementById('lat').value = currentLocation.lat(); //latitude
    document.getElementById('lng').value = currentLocation.lng(); //longitude
}








// Code to sync db output, python and script https://stackoverflow.com/questions/49718569/multiple-markers-in-flask-google-map-api
var map, i;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 7,
        center: new google.maps.LatLng(53.43237771764574, -6.871380403326448),
        mapTypeId: 'roadmap'
    });

    //variable to hold your endpoint
    var coordAddresses = 'https://8080-amethyst-crow-u769d91j.ws-eu03.gitpod.io/api/coordinates';
    //an array to hold your coordinates
    var locations = [];
    //Using fetch to process the ajax call 
    // if you use fetch, besure to include the source below this line in your template
    //<script src="https://cdnjs.cloudflare.com/ajax/libs/fetch/2.0.3/fetch.js"></script>
    fetch(coordAddresses)
        .then(function (response) {
            return response.text();
        }).then(function (body) {
            var obj = JSON.parse(body);
            var myAdd = {};
            var addresses = obj.coordinates;
            var l = addresses.length;
        
            for (i = 0; i < l; i++) {
                myAdd = {
                    position: {
                        lat: parseFloat(obj.coordinates[i].lat),
                        lng: parseFloat(obj.coordinates[i].lng)
                    },
                    title: obj.coordinates[i].title,
                };
                locations.push(myAdd);
            }
            locations.forEach(function (feature) {
                var marker = new google.maps.Marker({
                    position: feature.position,
                    title: feature.title,
                    map: map
                });
            });

        }).catch(function () {
            // if the ajax call fails display an error in an info window
            var pos = {
                lat: lat,
                lng: lng
            };
            infoWindow.setMap(map);
            infoWindow.setPosition(pos);
            infoWindow.setContent('An error occurred, we are unable to retrieve coordinates.');

        });

        // Second map for add_locaton_map window
        
}

google.maps.event.addDomListener(window, 'load', initMap);