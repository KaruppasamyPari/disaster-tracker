const USERNAME = "admin";
const PASSWORD = "1234";

function login() {
    let user = document.getElementById("username").value;
    let pass = document.getElementById("password").value;
    let errorMsg = document.getElementById("error");

    if (user === USERNAME && pass === PASSWORD) {
        document.getElementById("login-box").style.display = "none";
        document.getElementById("map-box").style.display = "block";
        loadMap();
    } else {
        errorMsg.innerText = "Invalid username or password!";
    }
}

var map;
var markers = {};

function loadMap() {
    map = L.map('map').setView([11.0, 77.0], 6);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);

    loadTeams();
    setInterval(loadTeams, 5000);
}

function loadTeams() {
    fetch("http://127.0.0.1:5000/get_teams")
    .then(res => res.json())
    .then(data => {
        data.forEach(team => {
            var color = team.role === "Medical" ? "red" : team.role === "Police" ? "blue" : "green";
            if (markers[team.id]) {
                map.removeLayer(markers[team.id]);
            }
            markers[team.id] = L.circleMarker([team.latitude, team.longitude], {
                color: color,
                radius: 8
            }).addTo(map).bindPopup(
                `<b>${team.name}</b><br>
                 Role: ${team.role}<br>
                 Contact: ${team.contact}<br>
                 Phone: ${team.phone}`
            );
        });
    });
}
