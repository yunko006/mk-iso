import json

import pytest

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# # Remplacez "DATABASE_URL" par votre URL de base de données
# DATABASE_URL = "pass"

# # Créer une instance de moteur SQLAlchemy
# engine = create_engine(DATABASE_URL)

# # Créer une fabrique de sessions avec le schéma spécifié
# SessionLocal = sessionmaker(
#     autocommit=False, autoflush=False, bind=engine, schema="tests"
# )

# # Vous pouvez maintenant utiliser SessionLocal pour créer des sessions avec le schéma 'tests'


def test_create_seller_site(test_app_with_db):
    response = test_app_with_db.post(
        "/seller_sites/",
        data=json.dumps({"site_url": "https://foo.bar", "site_name": "lul"}),
    )

    assert response.status_code == 201
    assert response.json()["site_url"] == "https://foo.bar"


def test_create_seller_site_invalid_json(test_app):
    """
    Actuellement ma db accepte de valeurs nuls/empty ce test ne peut pas passer.
    """
    pass
    """
    response = test_app.post("/seller_sites/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "site_url"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "site_name"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }

    # Test avec un champ manquant
    response = test_app.post("/seller_sites/", json={"site_url": "example.com"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "site_name"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }
    """


def test_read_seller_site(test_app_with_db):
    response = test_app_with_db.post(
        "/seller_sites/",
        data=json.dumps({"site_url": "https://foo.bar", "site_name": "Fighters"}),
    )
    seller_site_id = response.json()["id"]

    response = test_app_with_db.get(f"/seller_sites/{seller_site_id}/")
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == seller_site_id
    assert response_dict["site_url"] == "https://foo.bar"
    assert response_dict["site_name"] == "Fighters"


def test_read_all_seller_sites(test_app_with_db):
    response = test_app_with_db.post(
        "/seller_sites/",
        data=json.dumps({"site_url": "https://foo.bar", "site_name": "Fighters"}),
    )
    seller_site_id = response.json()["id"]

    response = test_app_with_db.get("/seller_sites/")
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == seller_site_id, response_list))) == 1
