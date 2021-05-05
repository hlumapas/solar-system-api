def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet_planet_is_there(client, three_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "name": "Earth",
        "description": "nice big rock",
        "id": 1
    }


def test_get_one_planet_with_no_records(client):
    response = client.get("/planets/1")

    assert response.status_code == 404
    assert response.get_data().decode("utf-8") == "Planet outside of the bounds of the universe :("
