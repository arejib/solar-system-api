from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

    def make_planet_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            color=self.color
        )

planets = [
    Planet(1, "Mercury", "1st planet from the Sun", "light blue"),
    Planet(2, "Venus", "2nd planet from the Sun", "orange"),
    Planet(3, "Earth", "3rd planet from the Sun", "black"),
    Planet(4, "Mars", "4th planet from the Sun", "red"),
    Planet(5, "Jupiter", "5th planet from the Sun", "green"),
    Planet(6, "Saturn", "6th planet from the Sun", "purple"),
    Planet(7, "Uranus", "7th planet from the Sun", "dark blue"),
    Planet(8, "Neptune", "8th planet from the Sun", "aqua"),
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"Planet {planet_id} is invalid."}, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    abort(make_response({"message": f"Planet {planet_id} not found."}, 404))
    
@planets_bp.route("", methods=["GET"])
def handle_planets():
    result_list = []
    for planet in planets:
        result_list.append(planet.make_planet_dict())
    return jsonify(result_list)

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.make_planet_dict()