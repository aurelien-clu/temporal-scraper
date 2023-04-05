import json
from urllib.parse import urlparse

import bs4
import httpx
from temporalio import activity

from scraper_model import FetchedPage, ParsedPage, SavePage


@activity.defn
async def fetch_page(url: str) -> FetchedPage:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        content_str = response.text
    return FetchedPage(url=url, html_body=content_str)


@activity.defn
async def parse_page(page: FetchedPage) -> ParsedPage:
    url_parsed = urlparse(page.url)

    def extract_title(soup):
        for title in soup.find_all("title"):
            return title.get_text()
        return ""

    def extract_links(soup):
        for node in soup.find_all("a"):
            link = node.get("href")
            if link.startswith("/"):
                link = url_parsed.netloc + link
            yield link

    soup = bs4.BeautifulSoup(page.html_body, features="html.parser")

    title = extract_title(soup)
    links = list(extract_links(soup))
    return ParsedPage(url=page.url, title=title, links=links)


@activity.defn
async def save_page(to_save: SavePage):
    with open(to_save.path, "w") as f:
        json.dump(to_save.page.__dict__, f, indent=4)
