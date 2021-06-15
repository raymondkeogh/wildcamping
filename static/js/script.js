$(document).ready(function () {

    $('.sidenav').sidenav({
        edge: "right"
    });
    $('input#input_text, textarea#location_description').characterCounter();
    $('input#input_text, textarea#location_name').characterCounter();
    $('.tooltipped').tooltip();
    setTimeout(function() {
        $('.flashes').fadeOut('slow');
    }, 4000);

});


document.addEventListener('DOMContentLoaded', function() {
    let elems = document.querySelectorAll('.tooltipped');
    let instances = M.Tooltip.init(elems);
  });


      
let add_location_map;
let marker2 = false;
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
        let clickedLocation = event.latLng;

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
    let currentLocation = marker2.getPosition();
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


// Draw map and add markers based on mongodb query results
function searchResultMap() {
    let locationsString = $('#search-coordinates').text()
    let nLocationsString = locationsString.replace(",]}", "]}");
    let locationsObj = JSON.parse(nLocationsString);
    let locations = locationsObj.coordinates;
    let loclen = locations.length;
    centerLat = locations[Math.floor(loclen / 2)].lat;
    centerLng = locations[Math.floor(loclen / 2)].lng;

    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 8,
        center: new google.maps.LatLng(centerLat, centerLng),
        mapTypeId: 'roadmap'
    });

    let coordinates = {
        lat: 40.785845,
        lng: -74.020496
    };

    let infowindow =  new google.maps.InfoWindow({
		content: ''
	});

    let contentString = 
    locations.forEach(function (feature) {
        let marker = new google.maps.Marker({
            title: feature.name,
            position: {
                "lat": feature.lat,
                "lng": feature.lng
            },
            map: map
        });
        // add an event listener for this marker
		bindInfoWindow(marker, map, infowindow,
            "<div class='info-window'>" +
            "<div class='campsite-pic'><img src=" + feature.file + "><h6>" + 
            feature.name + "</h6>" 
             + "<br>" 
             + "<p>" + feature.description + "</p>" +
            "</div>"
             ); 
    });
    // figuure out how to add triple quotes in above bindinfowindow
    // "<a href=\"{{ url_for('view_location', location_id="+ feature._id +")}}\">" +
    // function mark_pins(trucks) {
    //     let geocoder = new google.maps.Geocoder();
    //     let markersArray = [];
    //     for (i = 0; i < loclen; i++) {
    //         // iterate each address
    //         geocoder.geocode({
    //             'address': trucks[i]['address']
    //         }, function (results, status) {
    //             if (status == google.maps.GeocoderStatus.OK) {
    //                 let marker = new google.maps.Marker({
    //                     map: map,
    //                     position: results[0].geometry.location
    //                 });
    //                 marker.setMap(map);
    //                 bounds.extend(results[0].geometry.location);
    //                 map.fitBounds(bounds);
    //             } else {
    //                 alert('Internal error: ' + status + address);
    //             }
    //         });
    //     }
    // }
    // console.log(centerOfmyAdd);
 
}

function bindInfoWindow(marker, map, infowindow, html) { 
	google.maps.event.addListener(marker, 'click', function() { 
		infowindow.setContent(html); 
		infowindow.open(map, marker); 
	}); 
} 

function validateForm() {

    let location_name = document.forms["user_location_form"]["location_name"].value;
    let desc = document.forms["user_location_form"]["location_description"].value;
    let rating = document.forms["user_location_form"]["rating"].value;
    let coord = document.forms["user_location_form"]["lat"].value;

    if (location_name == "") {
        alert("Please add a Name for your location");
        return false;
    }
    if (desc == "") {
        alert("Please write a short description");
        return false;
    }
    if (rating == "") {
        alert("Please give your location a rating out of 5");
        return false;
    }

    if (coord == "") {
        alert("Please locate your campsite in the map window");
        return false;
    }
}



// google.maps.event.addDomListener(window, 'load', initialize);


