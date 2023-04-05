import httpx
from loguru import logger
from temporalio import activity

from scraper_model import FetchedPage, ParsedPage, SavePage
import bs4
from urllib.parse import urlparse

@activity.defn
async def fetch_page(url: str) -> FetchedPage:
    logger.debug(f"fetching, {url}!")
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        content_str = response.text
    return FetchedPage(url=url, html_body=content_str)


@activity.defn
async def parse_page(page: FetchedPage) -> ParsedPage:
    # TODO: find all links
    logger.debug(f"parsing!")
    title = ""

    url_parsed = urlparse(page.url)

    def extract_links(soup):
        for node in soup.find_all("a"):
            link = node.get('href')
            if link.startswith("/"):
                link = url_parsed.netloc + link
            yield link

    soup = bs4.BeautifulSoup(page.html_body, features="html.parser")
    links = list(extract_links(soup))

    for link in links:
        logger.debug(link)

    return ParsedPage(url=page.url, title=title, links=links)


@activity.defn
async def save_page(to_save: SavePage):
    logger.debug(f"saving page!")
