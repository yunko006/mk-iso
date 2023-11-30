# mk-iso

An app to discover and find ISO mechanical keyboards (mk).

## Why this project?

I am a mechanical keyboard enthusiast and found it challenging to locate good resources about ISO layout mechanical keyboards. To address this issue and enhance my skills, I decided to create this small app.

## Stack description

#### Automated Scraping of Keyboard Manufacturer Websites

- Utilizing Python & Beautiful Soup 4 for web scraping and adding data to the database.

> Currently, only a few manufacturer sites are scraped (Epomaker & Keychron).

#### Using Supabase as a PostgreSQL

- Design and development of a PostgreSQL database for storing extracted data.
- Employing Pydantic for data serialization and structured sending.
- Migrations are performed using Alembic.

#### Development of a Robust API to Consume, Process, and Redirect Data from the Database to the Frontend

- The API is built with Python & FastAPI, with public endpoints: get & get_all.
- All development endpoints can be found [here](backend/app/api/endpoints.md).
- Only the scraper can create news keyboards/descriptions.

## Folder organization

- Backend:
  - Everything related to the API, database, and migrations.
  - I followed the CRUD/schemas/models approach to separate actions into different files.
  - Used Sqlalchemy & Alembic to interact with the database and perform migrations.

- Frontend:
  - Contains all files for the frontend; it will be a basic ReactJS app.

- Scrape:
  - This is where my scraper resides. I took a class-based approach to develop my scraper; all my SiteScrapers will inherit from my base class: [ScrapeKbFromKeyboardModel](scrape/scrape_from_db.py).
  - Used Pydantic to serialize the data sent to the database to ensure that the data can be easily consumed by the API.

## What's next? / TODO List

- [ ] Deploy the app. Where?
- [ ] Dockerize the scraper and deploy it to my Raspberry Pi 4.
- [ ] Implement a cron job to trigger the scraper at specific times.
- [ ] Plan to add a way for users to request a seller_site to be scraped and added to the database.
- [ ] Create a basic frontend with ReactJS.
- [ ] Refactor the scrape folder; consider adding subfolders.

## Link to technologies used

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Supabase](https://supabase.com/)
- [Beautiful Soup 4](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Docker](https://www.docker.com/)
- [Pytest](https://docs.pytest.org/en/7.4.x/)

## Credit

To [keeb-finder](https://keeb-finder.com/) for inspiring the creation of a mechanical keyboard site with only ISO layouts. I found some mistakes on keeb finder regarding ISO layout, like some keyboards are tagged as ISO layout but aren't.
