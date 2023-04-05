import asyncio

import fire
from temporalio.client import Client
import uuid

# Import the workflow from the previous code
from scraper_workflows import CrawlWebsite


async def async_crawl(url: str):
    url = "https://news.yahoo.com/"

    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        CrawlWebsite.run,
        url,
        id=uuid.uuid4().hex,
        task_queue="scraper",
    )

    print(f"Result: {result}")


def crawl(url: str):
    return asyncio.run(async_crawl(url=url))


if __name__ == "__main__":
    fire.Fire(crawl)
