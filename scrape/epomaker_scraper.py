import requests
from bs4 import BeautifulSoup

from schemas import EpomakerScrapeResults
from database import get_db
from crud import add_keyboard


class EpomakerScraper:
    def __init__(self):
        self.url = "https://epomaker.com/collections/iso-keyboard"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def _get_soup(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        else:
            raise Exception(
                f"La requête a échoué avec le code d'état {response.status_code}"
            )

    def get_name(self, keyboard):
        name = keyboard.find("a", {"class": "sf__pcard-name"}).text.strip()
        return name

    def get_price(self, keyboard):
        price = keyboard.find(
            "span", {"class": "f-price-item f-price-item--regular"}
        ).text.strip()
        return price

    def get_url(self, keyboard):
        product_link = keyboard.find(
            "a",
            {"class": "sf__pcard-name"},
        )["href"]

        full_product_link = (
            "https://www.epomaker.com" + product_link
            if not product_link.startswith("http")
            else product_link
        )
        return full_product_link

    # main function
    def scrape_keyboards(self) -> EpomakerScrapeResults:
        soup = self._get_soup()
        keyboards = []
        db = get_db()

        for keyboard in soup.find_all(
            "div", {"class": "sf__col-item w-6/12 md:w-4/12 px-2 xl:px-3"}
        ):
            name = self.get_name(keyboard)
            price = self.get_price(keyboard)
            product_link = self.get_url(keyboard)

            # Créer une instance de EpomakerScrapeResults au lieu d'un dictionnaire
            payload = EpomakerScrapeResults(
                name=name, url=product_link, price=float(price[1:]), image=None
            )

            add_keyboard(db, payload)

        return keyboards


if __name__ == "__main__":
    scraper = EpomakerScraper()

    scraper.scrape_keyboards()
