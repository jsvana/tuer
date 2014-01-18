var Map = {};

Map.initmap = function() {
	Map.map = new L.Map('map');

	var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
	var osmAttrib = 'Map data © OpenStreetMap contributors';
	var osm = new L.TileLayer(osmUrl, {
		minZoom: 8,
		maxZoom: 12,
		attribution: osmAttrib
	});

	/*
	var lat = $('#lat').val();
	var lng = $('#lng').val();
	*/
	var lat = 42;
	var lng = 88;

	Map.map.setView(new L.LatLng(lat, lng), 9);
	Map.map.addLayer(osm);

	Map.marker = L.marker([lat, lng]).addTo(Map.map);
};

$(function() {
	Map.initmap();
});
