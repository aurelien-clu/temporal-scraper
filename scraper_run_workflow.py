import asyncio

from temporalio.client import Client

# Import the workflow from the previous code
from scraper_workflows import CrawlWebsite


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        CrawlWebsite.run, "my name", id="my-workflow-id", task_queue="scraper"
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
