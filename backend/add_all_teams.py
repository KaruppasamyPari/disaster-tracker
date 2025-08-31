import requests
import random

url = "http://127.0.0.1:5000/update_location"

# City centers
cities = {
    "Chennai": {"lat": 13.0827, "lon": 80.2707, "count": 10},
    "Madurai": {"lat": 9.9252, "lon": 78.1198, "count": 5},
    "Coimbatore": {"lat": 11.0168, "lon": 76.9558, "count": 5},
    "Trichy": {"lat": 10.7905, "lon": 78.7047, "count": 5},
    "Rajapalayam": {"lat": 9.4520, "lon": 77.5536, "count": 2}
}

roles = ["Medical", "Police", "Volunteer"]
teams = []
team_id = 1

for city, data in cities.items():
    for i in range(1, data["count"] + 1):
        role = random.choice(roles)
        teams.append({
            "id": team_id,
            "name": f"{city} Team {i}",
            "role": role,
            "contact": "Karuppasamy",
            "phone": "9345583758",
            "latitude": data["lat"] + random.uniform(-0.05, 0.05),
            "longitude": data["lon"] + random.uniform(-0.05, 0.05)
        })
        team_id += 1

for team in teams:
    r = requests.post(url, json=team)
    print(team["name"], team["role"], r.json())
