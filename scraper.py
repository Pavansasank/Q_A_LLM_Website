from urllib import response

import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    
    print("SCRAPING:", url)

    response = requests.get(
        url,
        timeout=20,
        headers={
            "User-Agent":
            "Mozilla/5.0"
        }
    )

    print("STATUS:", response.status_code)

    if response.status_code != 200:
        raise Exception(
            f"Failed to load website. Status code: {response.status_code}"
        )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    text = soup.get_text(
        separator=" ",
        strip=True
    )

    return text