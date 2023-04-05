from datetime import timedelta

from temporalio import workflow

# Import our activity, passing it through the sandbox
with workflow.unsafe.imports_passed_through():
    from scraper_activities import fetch_page, parse_page, save_page


@workflow.defn
class CrawlWebsite:
    @workflow.run
    async def run(self, url: str) -> str:
        page = await workflow.execute_activity(
            fetch_page, url, schedule_to_close_timeout=timedelta(seconds=5)
        )
        parsed = await workflow.execute_activity(
            parse_page, page, schedule_to_close_timeout=timedelta(seconds=5)
        )
        await workflow.execute_activity(
            save_page, parsed, schedule_to_close_timeout=timedelta(seconds=5)
        )
        return "done"
