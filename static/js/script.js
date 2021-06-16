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


  let marker2 = false;

  function initAutocomplete() {
    const map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: -33.8688, lng: 151.2195 },
      zoom: 13,
      mapTypeId: "roadmap",
      disableDefaultUI: true
    });
    // Create the search box and link it to the UI element.
    const input = document.getElementById("pac-input");
    const searchBox = new google.maps.places.SearchBox(input);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    // Bias the SearchBox results towards current map's viewport.
    map.addListener("bounds_changed", () => {
      searchBox.setBounds(map.getBounds());
    });
    let markers = [];
    // Listen for the event fired when the user selects a prediction and retrieve
    // more details for that place.
    searchBox.addListener("places_changed", () => {
      const places = searchBox.getPlaces();
  
      if (places.length == 0) {
        return;
      }
      // Clear out the old markers.
      markers.forEach((marker) => {
        marker.setMap(null);
      });
      markers = [];
      // For each place, get the icon, name and location.
      const bounds = new google.maps.LatLngBounds();
      places.forEach((place) => {
        if (!place.geometry || !place.geometry.location) {
          console.log("Returned place contains no geometry");
          return;
        }
        const icon = {
          url: place.icon,
          size: new google.maps.Size(71, 71),
          origin: new google.maps.Point(0, 0),
          anchor: new google.maps.Point(17, 34),
          scaledSize: new google.maps.Size(25, 25),
        };
        // Create a marker for each place.
        markers.push(
          new google.maps.Marker({
            map,
            icon,
            title: place.name,
            position: place.geometry.location,
          })
        );
  
        if (place.geometry.viewport) {
          // Only geocodes have viewport.
          bounds.union(place.geometry.viewport);
        } else {
          bounds.extend(place.geometry.location);
        }
      });
      map.fitBounds(bounds);
    });
    google.maps.event.addListener(map, 'click', function (event) {
        //Get the location that the user clicked.
        let clickedLocation = event.latLng;

        //If the marker hasn't been added
        if (marker2 === false) {
            //Create the marker.
            marker2 = new google.maps.Marker({
                position: clickedLocation,
                map: map,
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
        fetch_format: auto
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
    let firstString = locationsString.replace(/\s+/g,' ').trim();
    let nLocationsString = firstString.replace(",]}", "]}");
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


// File Size validation
// https://www.encodedna.com/jquery/get-file-size-before-uploading-using-javascript-and-jquery.html

function GetFileSize() {
let fi = document.getElementById('media'); // GET THE FILE INPUT.

// VALIDATE OR CHECK IF ANY FILE IS SELECTED.
if (fi.files.length > 0) {
    // RUN A LOOP TO CHECK EACH SELECTED FILE.
    for (let i = 0; i <= fi.files.length - 1; i++) {
        let fsize = fi.files.item(i).size; // THE SIZE OF THE FILE.
      console.log(fsize)

      if (fsize >= 10485760) {
        alert("File size too big, please upload a smaller file");
          return false;
      }
      
      document.getElementById('fp').innerHTML =
            document.getElementById('fp').innerHTML + '<br /> ' +
                '<b>' + "File Size: " + Math.round((fsize / 1024)) + '</b> KB';
      document.user_location_image.submit()
    }
}
}

// google.maps.event.addDomListener(window, 'load', initialize);


