let map;

function initMap() {
    const myLatLng = { lat: -25.363, lng: 131.044 };
    const myLatLng2 = { lat: 50.363, lng: 150.044 };
    const myLatLng3 = { lat: 50.345, lng: 25.24 };
    const myLatLng4 = { lat: 67.54, lng: 27.865};
    const img =
    "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";

    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 32.7502, lng: 40.7655 },
        zoom: 2,
    });
    const marker = new google.maps.Marker({
        position: myLatLng,
        map,
        title: "Hello World!",
        icon: img,
    });
    const marker1 = new google.maps.Marker({
        position: myLatLng2,
        map,
        title: "Second Marker!",
        icon: img,
    });
    const marker2 = new google.maps.Marker({
        position: myLatLng3,
        map,
        title: "Third Marker!",
        icon: img,
    });
    const marker3 = new google.maps.Marker({
        position: myLatLng4,
        map,
        title: "Four!",
        icon: img,
    });
    flightPlanCoordinates = [
        myLatLng,
        myLatLng2,
        myLatLng3,
        myLatLng4,
    ]

    const flightPath = new google.maps.Polyline({
        path: flightPlanCoordinates,
        geodesic: true,
        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 2,
    });

    flightPath.setMap(map);

    marker.addListener("click", () => {
        map.setZoom(8);
        map.setCenter(marker.getPosition());
    });
    marker1.addListener("click", () => {
        map.setZoom(8);
        map.setCenter(marker1.getPosition());
    });
}