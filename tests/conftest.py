import pytest
from app import create_app
from app import db
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def three_saved_planets(app):
    earth = Planet(name="Earth", description="nice big rock")
    pluto = Planet(name="Pluto", description="am I a planet tho?")
    mars = Planet(name="Mars", description="I have robots on me")

    db.session.add_all([earth, pluto, mars])
    db.session.commit()
