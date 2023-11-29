from models import Keyboard, SellerSite, Description


def add_keyboard(db, payload):
    keyboard = Keyboard(
        name=payload.name, url=payload.url, price=payload.price, image=payload.image
    )
    db.add(keyboard)
    db.commit()
    db.refresh(keyboard)

    seller_site_id = payload.seller_site_id
    seller_site = db.query(SellerSite).filter(SellerSite.id == seller_site_id).first()

    if seller_site:
        keyboard.seller_site = seller_site
        db.commit()
        db.refresh(keyboard)

    db.close()


def add_description(db, payload, keyboard_id):
    description = Description(
        brand=payload.brand,
        layout=payload.layout,
        product_type=payload.product_type,
        profile=payload.profile,
        layout_size=payload.layout_size,
        layout_standard=payload.layout_standard,
        layout_ergonomics=payload.layout_ergonomics,
        hot_swappable=payload.hot_swappable,
        knob_support=payload.knob_support,
        rgb_support=payload.rgb_support,
        display_support=payload.display_support,
        qmk_via_support=payload.qmk_via_support,
        connection=payload.connection,
        battery_capacity=payload.battery_capacity,
        mount_style=payload.mount_style,
        case_material=payload.case_material,
        keycap_material=payload.keycap_material,
    )

    db.add(description)
    db.commit()
    db.refresh(description)

    kb_id = keyboard_id
    keyboard = db.query(Keyboard).filter(Keyboard.id == kb_id).first()

    if keyboard:
        description.keyboard = keyboard
        db.commit()
        db.refresh(keyboard)
