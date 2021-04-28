$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    });
});


let map;
// Google maps api
function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {
            lat: -34.397,
            lng: 150.644
        },
        zoom: 8,
    });
}