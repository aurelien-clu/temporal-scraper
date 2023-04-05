from temporalio import activity
from loguru import logger


@activity.defn
async def fetch_page(url: str) -> str:
    logger.info(f"fetching, {url}!")
    return "<html>Empty</html>"

@activity.defn
async def parse_page(page: str) -> str:
    logger.info(f"fetching, {page}!")
    return "Empty"

@activity.defn
async def save_page(parsed_page: str):
    logger.info(f"saving, {parsed_page}!")
