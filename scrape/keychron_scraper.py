import time
import requests
from bs4 import BeautifulSoup


class KeychronScraper:
    def __init__(self):
        self.url = (
            "https://www.keychron.com/collections/keychron-iso-jis-keyboard-collection"
        )
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def _get_soup(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "lxml")
        else:
            raise Exception(
                f"La requête a échoué avec le code d'état {response.status_code}"
            )

    def _scroll_down(self):
        # Simulez le défilement en faisant plusieurs requêtes successives
        for _ in range(5):
            # Répétez cela selon le nombre de fois que vous souhaitez scroller
            response = requests.get(self.url, headers=self.headers)
            time.sleep(1)  # Attendez un court instant pour que le contenu se charge

    def get_name(self, keyboard):
        name = keyboard.find(
            "a", {"class": "card-link text-current js-prod-link"}
        ).text.strip()
        return name

    def get_price(self, keyboard):
        price = keyboard.find("strong", {"class": "price__current"}).text.strip()
        # price__current
        return price

    def get_url(self, keyboard):
        product_link = keyboard.find(
            "a", {"class": "card-link text-current js-prod-link"}
        )["href"]
        full_product_link = (
            "https://www.keychron.com" + product_link
            if not product_link.startswith("http")
            else product_link
        )
        return full_product_link

    # main function
    def scrape_keyboards(self):
        self._scroll_down()
        soup = self._get_soup()
        keyboards = []

        for keyboard in soup.find_all("li", {"class": "js-pagination-result"}):
            name = self.get_name(keyboard)
            price = self.get_price(keyboard)
            product_link = self.get_url(keyboard)

            keyboards.append(
                {"name": name, "price": price, "product_link": product_link}
            )

        return keyboards


# Exemple d'utilisation de la classe KeychronScraper
scraper = KeychronScraper()

keyboards = scraper.scrape_keyboards()

for keyboard in keyboards:
    print(f"Nom: {keyboard['name']}")
    print(f"Prix: {keyboard['price']}")
    print(f"URL de la page: {keyboard['product_link']}")
    print("\n")
