import json


def test_create_keyboard(client):
    response = client.post(
        "/keyboards/",
        data=json.dumps(
            {
                "name": "test",
                "url": "test",
                "price": 0,
                "image": "test",
                "seller_site_id": 2,
                "description": {
                    "layout": "string",
                    "brand": "string",
                    "product_type": "string",
                    "profile": "string",
                    "layout_size": "string",
                    "layout_standard": "string",
                    "layout_ergonomics": "string",
                    "hot_swappable": True,
                    "knob_support": True,
                    "rgb_support": True,
                    "display_support": True,
                    "qmk_via_support": True,
                    "connection": "string",
                    "battery_capacity": "string",
                    "mount_style": "string",
                    "case_material": "string",
                    "keycap_material": "string",
                },
            }
        ),
    )

    assert response.status_code == 201
    assert response.json()["url"] == "test"


def test_create_keyboard_invalide_data(client):
    pass


def test_read_one_keyboard(client):
    pass


def test_read_bad_keyboard(client):
    pass


def test_read_all_keyboard(client):
    pass


def test_put_name_keyboard(client):
    pass


def test_put_url_keyboard(client):
    pass


def test_put_price_keyboard(client):
    pass
