import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

# Import the activity and workflow from our other files
from scraper_activities import *
from scraper_workflows import *


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Run the worker
    worker = Worker(
        client, 
        task_queue="scraper", 
        workflows=[CrawlWebsite], 
        activities=[
            fetch_page,
            parse_page,
            save_page,
        ],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
