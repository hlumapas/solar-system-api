def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_all_planets_with_records(client, three_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "name": "Earth",
        "description": "nice big rock",
        "id": 1
    },{
    
        "name": "Pluto",
        "description": "am I a planet tho?",
        "id": 2
    },{
    
        "name": "Mars",
        "description": "I have robots on me",
        "id": 3
    }]


def test_post_new_planet(client):
    response = client.post("/planets", json={"name":"Mercury", "description":"its color is boring gray"})
    
    assert response.status_code == 201
    assert response.get_data().decode("utf-8") == "Planet Mercury successfully created" 

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
