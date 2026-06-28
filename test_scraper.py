from scraper import scrape_website


url = "https://fastapi.tiangolo.com/"

content = scrape_website(url)

print(content[:2000])

print(len(content))