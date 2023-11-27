from models import Keyboard, SellerSite


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
