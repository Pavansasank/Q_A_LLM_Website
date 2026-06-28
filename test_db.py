from scraper import scrape_website
from db import add_documents


url = "https://fastapi.tiangolo.com/"

content = scrape_website(url)

count = add_documents(content)

print(
    f"{count} chunks stored."
)