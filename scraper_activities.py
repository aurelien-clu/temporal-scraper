import httpx
from loguru import logger
from temporalio import activity


@activity.defn
async def fetch_page(url: str) -> str:
    logger.info(f"fetching, {url}!")
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
    return "<html>Empty</html>"


@activity.defn
async def parse_page(page: str) -> str:
    logger.info(f"fetching, {page}!")
    return "Empty"


@activity.defn
async def save_page(parsed_page: str):
    logger.info(f"saving, {parsed_page}!")
