import asyncio
import uuid

import fire
from temporalio.client import Client

from scraper_model import CrawlUrl
from scraper_workflows import CrawlWebsite


async def async_crawl(url: str, output_dir: str):
    crawl_cmd = CrawlUrl(url=url, output_dir=output_dir)

    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        CrawlWebsite.run,
        crawl_cmd,
        id=uuid.uuid4().hex,
        task_queue="scraper",
    )

    print(f"Result: {result}")


def crawl(url: str, output_dir: str):
    future = async_crawl(url=url, output_dir=output_dir)
    return asyncio.run(future)


if __name__ == "__main__":
    fire.Fire(crawl)
