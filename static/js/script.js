$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
});

$(document).ready(function () {
    $('input#input_text, textarea#location_description').characterCounter();
    $('input#input_text, textarea#location_name').characterCounter();
});
var add_location_map;
var marker2 = false;
// Second map for add_location_map window
// Created a second function as initializing the maps in 
// one func resulted in DOM errors and no maps display
function initUserMap() {
    // Tutorial that helped create marker locations 
    // https://thisinterestsme.com/google-maps-api-location-picker-example/

    add_location_map = new google.maps.Map(document.getElementById('add_location_map'), {
        center: new google.maps.LatLng(52.357971, -6.516758),
        zoom: 7,
        mapTypeId: 'roadmap'
    });

    google.maps.event.addListener(add_location_map, 'click', function (event) {
        //Get the location that the user clicked.
        var clickedLocation = event.latLng;
        
        //If the marker hasn't been added
        if (marker2 === false) {
            //Create the marker.
            marker2 = new google.maps.Marker({
                position: clickedLocation,
                map: add_location_map,
                draggable: true //make it draggable
            });
            //Listen for drag events!
            google.maps.event.addListener(marker2, 'dragend', function (event) {
                markerLocation();
            });
        } else {
            //Marker has already been added, so just change its location.
            marker2.setPosition(clickedLocation);
        }
        //Get the marker's location.
        markerLocation();
    });
}


function markerLocation() {
    //Get location.
    var currentLocation = marker2.getPosition();
    //Add lat and lng values to a field that we can save.
    document.getElementById('lat').value = currentLocation.lat(); //latitude
    document.getElementById('lng').value = currentLocation.lng(); //longitude
}

// Cloudinary File upload service
document.querySelector("form").addEventListener("submit", (event) => {
    // event.preventDefault();
    const fileInput = document.querySelector("#media");
    const formData = new FormData();

    formData.append("file", fileInput.files[0]);

    const options = {
        method: "POST",
        body: formData,
    };

    fetch("http://127.0.0.1:5000/upload", options)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log(data);
        })
        .catch((error) => {
            console.log(error);
        });
});

// Function to catch the like click event and send post to python
//https://stackoverflow.com/questions/62243087/in-django-how-to-send-json-object-using-xmlhttprequest-in-javascript
function likeMe(id) {
    $.ajax({
        url: "/likes",
        type: "POST",
        data: { locations : id },
        dataType: "json",
        success: function (result) {
            switch (result) {
                case true:
                    processResponse(result);
                    break;
                default:
                    resultDiv.html(result);
            }
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status);
            alert(thrownError);
        }
    });

}

// Draw map and add markers based on mongodb query results
function searchResultMap() {
    var locationsString = $('#search-coordinates').text()
    var nLocationsString = locationsString.replace(",]}", "]}");
    var locationsObj = JSON.parse(nLocationsString);
    var locations = locationsObj.coordinates
    var loclen = locations.length

    centerLat = locations[Math.floor(loclen/2)].lat;
    centerLng = locations[Math.floor(loclen/2)].lng;
           
            // console.log(centerOfmyAdd);
            map = new google.maps.Map(document.getElementById('map'), {
                zoom: 8,
                center: new google.maps.LatLng(centerLat, centerLng),
                mapTypeId: 'roadmap'
            });

            var coordinates = { lat: 40.785845, lng: -74.020496 };
            locations.forEach(function (feature) {
                var marker = new google.maps.Marker({
                    position: {"lat":feature.lat, "lng": feature.lng},
                    map: map
                });
            });
}



