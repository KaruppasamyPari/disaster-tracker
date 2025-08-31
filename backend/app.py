from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from math import radians, cos, sin, asin, sqrt
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class RescueTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    role = db.Column(db.String(50))
    contact = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    last_updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)

with app.app_context():
    db.create_all()

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    return 6371 * c

@app.route("/update_location", methods=["POST"])
def update_location():
    data = request.json
    team = RescueTeam.query.filter_by(id=data["id"]).first()
    if not team:
        team = RescueTeam(id=data["id"], name=data["name"], role=data["role"])
        db.session.add(team)
    team.latitude = data["latitude"]
    team.longitude = data["longitude"]
    team.contact = "Karuppasamy"
    team.phone = "9345583758"
    team.last_updated = datetime.datetime.utcnow()
    db.session.commit()
    return jsonify({"status": "success"})

@app.route("/get_teams", methods=["GET"])
def get_teams():
    teams = RescueTeam.query.all()
    return jsonify([{
        "id": t.id,
        "name": t.name,
        "role": t.role,
        "contact": t.contact,
        "phone": t.phone,
        "latitude": t.latitude,
        "longitude": t.longitude,
        "last_updated": t.last_updated.strftime("%Y-%m-%d %H:%M:%S")
    } for t in teams])

if __name__ == "__main__":
    app.run(debug=True)
