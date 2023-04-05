import asyncio

import fire
from temporalio.client import Client
from temporalio.worker import Worker

from scraper_activities import *
from scraper_workflows import *


async def async_start_worker(temporal_server: str, task_queue: str):
    client = await Client.connect(temporal_server)

    worker = Worker(
        client,
        task_queue=task_queue,
        workflows=[CrawlWebsite],
        activities=[
            fetch_page,
            parse_page,
            save_page,
        ],
    )
    await worker.run()


def start_worker(
    temporal_server: str = "localhost:7233",
    task_queue="scraper",
):
    future = async_start_worker(
        temporal_server=temporal_server,
        task_queue=task_queue,
    )
    return asyncio.run(future)


if __name__ == "__main__":
    fire.Fire(start_worker)
