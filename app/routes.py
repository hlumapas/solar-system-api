from flask import request, Blueprint, make_response, jsonify
from app import db
from app.models.planet import Planet


planets_bp = Blueprint(
    "planets",
    __name__,
    url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def list_planets():
    planets = Planet.query.all()
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        })
    return jsonify(planets_response)


@planets_bp.route("", methods=["POST"], strict_slashes=False)
def add_new_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("/<int:planet_id>", methods=["GET"], strict_slashes=False)
def get_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        planet_response = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        }
        return jsonify(planet_response)

    return make_response(
        "Planet outside of the bounds of the universe :(", 404)


@planets_bp.route("/<int:planet_id>", methods=["PUT"], strict_slashes=False)
def update_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        request_body = request.get_json()

        planet.name = request_body["name"]
        planet.description = request_body["description"]

        db.session.commit()

        return make_response(f"Planet {planet.name} successfully updated", 200)

    return make_response(
        "Planet outside of the bounds of the universe :(", 404)


@planets_bp.route("/<int:planet_id>", methods=["DELETE"], strict_slashes=False)
def delete_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        db.session.delete(planet)
        db.session.commit()
        return make_response(
            f"Planet {planet.name} was successfully deleted.", 200)

    return make_response(
        "Planet outside of the bounds of the universe :(", 404)


@planets_bp.route("/<string:planet_id>",
                  methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def get_not_int_planet_id():
    return make_response(
        "Bad request, please enter an integer after 'planets/'", 400)
