var initMap = function(pos) {
	var map = new L.Map('map');

	var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
	var osmAttrib = 'Map data © OpenStreetMap contributors';
	var osm = new L.TileLayer(osmUrl, {
		minZoom: 4,
		maxZoom: 12,
		attribution: osmAttrib
	});

	map.setView(new L.LatLng(pos.coords.latitude, pos.coords.longitude), 9);
	map.addLayer(osm);
};

$(function() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(initMap);
	} else {
		// Set default location
		var pos = {
			coords: {
				latitude: 42.3314,
				longitude: 83.0458
			}
		};

		initMap(pos);
	}
});
