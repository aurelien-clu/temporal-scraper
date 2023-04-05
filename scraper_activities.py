import httpx
from loguru import logger
from temporalio import activity

from scraper_model import FetchedPage, ParsedPage, SavePage


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
    # TODO: define dataclass inputs & outputs of each activity
    logger.debug(f"parsing!")
    title = ""
    links = []

    return ParsedPage(url=page.url, title=title, links=links)


@activity.defn
async def save_page(to_save: SavePage):
    logger.debug(f"saving page!")
