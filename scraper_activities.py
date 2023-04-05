import httpx
from loguru import logger
from temporalio import activity


@activity.defn
async def fetch_page(url: str) -> str:
    logger.info(f"fetching, {url}!")
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        content_str = response.text
    return content_str


@activity.defn
async def parse_page(page: str) -> str:
    logger.info(f"parsing page.length={len(page)}!")
    return "Empty"


@activity.defn
async def save_page(parsed_page: str):
    logger.info(f"saving parsed_page.length={len(parsed_page)}!")
