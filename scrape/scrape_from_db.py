# prends les url qui sont dans le model Keyboard, les parcours et extrait les descriptions pour le model: Description
from typing import Dict
import requests
from bs4 import BeautifulSoup


from models import Keyboard, Description
from database import get_db
from crud import add_description
from schemas import DescriptionScrapeResults


class ScrapeKbFromKeyboardModel:
    def __init__(self) -> None:
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.db = get_db()

    def _get_soup(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        else:
            raise Exception(
                f"La requête a échoué avec le code d'état {response.status_code}"
            )

    def scrape_description_from_keyboard_url(self, keyboard_model):
        """
        prends un url du model Keyboard,
        extrait les données de description et
        commit les données dans le model Description.
        """
        db = self.db

        try:
            # Récupérez le Keyboard depuis la base de données en utilisant le modèle passé en paramètre
            keyboard = db.query(Keyboard).filter_by(url=keyboard_model.url).first()

            if keyboard:
                url = keyboard.url

                # Utilisez la nouvelle fonction _get_soup avec l'URL en paramètre
                soup = self._get_soup(url)

                # Exemple : extraire le titre de la page
                title = soup.title.text
                print(f"Titre de la page pour {keyboard.name}: {title}")

                # Continuez à extraire d'autres informations selon vos besoins

            else:
                print(
                    f"Le clavier avec l'URL {keyboard_model.url} n'a pas été trouvé dans la base de données."
                )

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

    def scrape_all_keyboards(self):
        """
        Parcours tous les url et utilise la fonction :
        scrape_description_from_keyboard_url pour ajouter
        chaque description de kb.
        """
        # Utilisez la session SQLAlchemy préalablement créée dans le constructeur
        db = self.db

        try:
            # prendre les kb qui appartiennent a Epomaker
            keyboards = db.query(Keyboard).all()

            # Parcourez chaque enregistrement et scrapez les données à partir de l'URL
            for keyboard_model in keyboards:
                self.scrape_description_from_keyboard_url(keyboard_model)

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")


class EpomakerScraper(ScrapeKbFromKeyboardModel):
    SELLER_SITE_ID = 2
    """epomaker utilise une table pour stocker toutes les infos donc scraping en consequence."""

    def _get_tech_spec(self, tech_specs, *keys, default="pas spécifié"):
        """
        fonction utils
        """
        for key in keys:
            value = tech_specs.get(key)
            if value is not None:
                return value
        return default

    def _find_tech_specs_container(self, soup):
        """
        fonction utils qui permet de trouver la table sur la page.
        """
        return soup.find("div", class_="product---technicalspecs")

    def _extract_tech_specs(self, container) -> Dict:
        """
        fonction utils qui permet d'extraire tous les champs dans un dict.
        """
        tech_specs = {}
        data_rows = container.find_all("div", class_="data-row")

        for row in data_rows:
            title = row.find("div", class_="data-row-title").text.strip()
            description = row.find("div", class_="data-row-description").text.strip()
            tech_specs[title] = description

        return tech_specs

    def scrape_tech_specs(self, url) -> DescriptionScrapeResults:
        """
        logique :
        scrape la table de description de epomaker
        return : la class DescriptionScrapeResults pour etre utiliser par
                la fonction main pour inserer chaque donnée dedans.
        """
        try:
            soup = self._get_soup(url)
            container = self._find_tech_specs_container(soup)

            if container:
                tech_specs = self._extract_tech_specs(container)

                payload = DescriptionScrapeResults(
                    layout=self._get_tech_spec(tech_specs, "Layout", "LAYOUT"),
                    brand=self._get_tech_spec(tech_specs, "Brand", "Model"),
                    product_type="keyboard",
                    profile=self._get_tech_spec(
                        tech_specs,
                        "Keycap Profile",
                    ),
                    layout_size=self._get_tech_spec(tech_specs, "Layout", "LAYOUT"),
                    layout_standard="ISO",
                    layout_ergonomics="",
                    hot_swappable=self._get_tech_spec(
                        tech_specs,
                        "Hot-swappable",
                        "Hotswappable",
                        "HOT-SWAPPABLE",
                        "Hot-swap",
                    ),
                    knob_support=True,
                    rgb_support=True,
                    display_support=True,
                    qmk_via_support=True,
                    connection=self._get_tech_spec(
                        tech_specs, "CONNECTIVITY", "Connectivity"
                    ),
                    battery_capacity=self._get_tech_spec(
                        tech_specs, "Battery Capacity", "Battery capacity"
                    ),
                    mount_style=self._get_tech_spec(
                        tech_specs,
                        "Mount Type",
                    ),
                    case_material=self._get_tech_spec(
                        tech_specs, "Material", "PLATE MATERIAL", "Case Material"
                    ),
                    keycap_material=self._get_tech_spec(
                        tech_specs, "KEYCAPS", "Keycap Material"
                    ),
                )

                return payload

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

        return None

    def scrape_all_epomaker_keyboards(self):
        """
        Parcours tous les url et utilise la fonction :
        scrape_description_from_keyboard_url pour ajouter
        chaque description de kb.
        """
        db = self.db

        try:
            # prendre les kb qui appartiennent a Epomaker
            keyboards = (
                db.query(Keyboard)
                .filter(Keyboard.seller_site_id == self.SELLER_SITE_ID)
                .all()
            )

            # Parcourez chaque enregistrement et scrapez les données à partir de l'URL
            for keyboard_model in keyboards:
                payload = self.scrape_tech_specs(keyboard_model.url)
                if payload:
                    print(payload)
                    kb_id = keyboard_model.id
                    add_description(db, payload, kb_id)

        except Exception as e:
            print(f"Une erreur s'est produite : {e}")


if __name__ == "__main__":
    epomaker_scraper = EpomakerScraper()
    epomaker_scraper.scrape_all_epomaker_keyboards()
