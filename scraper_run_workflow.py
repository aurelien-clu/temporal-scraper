import asyncio
import os
import uuid

import fire
from loguru import logger
from temporalio.client import Client

from scraper_model import CrawlUrl
from scraper_workflows import CrawlWebsite


async def async_crawl(
    url: str,
    output_dir: str,
    temporal_server: str,
    task_queue: str,
):
    id_ = uuid.uuid4().hex

    crawl_cmd = CrawlUrl(
        id=id_,
        url=url,
        sep=os.sep,
        output_dir=output_dir,
    )

    # Create client connected to server at the given address
    client = await Client.connect(temporal_server)

    # Execute a workflow
    logger.info(f"starting: {crawl_cmd}...")
    result = await client.execute_workflow(
        CrawlWebsite.run,
        crawl_cmd,
        id=id_,
        task_queue=task_queue,
    )

    logger.success(f"{result}")


def crawl(
    url: str,
    output_dir: str,
    temporal_server: str = "localhost:7233",
    task_queue="scraper",
):
    future = async_crawl(
        url=url,
        output_dir=output_dir,
        temporal_server=temporal_server,
        task_queue=task_queue,
    )
    return asyncio.run(future)


if __name__ == "__main__":
    fire.Fire(crawl)
