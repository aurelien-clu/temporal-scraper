from datetime import timedelta

from temporalio import workflow

# Import our activity, passing it through the sandbox
with workflow.unsafe.imports_passed_through():
    from scraper_activities import fetch_page, parse_page, save_page
    from scraper_model import CrawlUrl, FetchedPage, OutputStats, ParsedPage, SavePage


@workflow.defn
class CrawlWebsite:
    @workflow.run
    async def run(self, cmd: CrawlUrl) -> OutputStats:
        workflow.logger.info(f"fetching {cmd.url}...")
        page: FetchedPage = await workflow.execute_activity(
            fetch_page,
            cmd.url,
            schedule_to_close_timeout=timedelta(seconds=5),
        )

        parsed: ParsedPage = await workflow.execute_activity(
            parse_page,
            page,
            schedule_to_close_timeout=timedelta(seconds=5),
        )
        workflow.logger.info(
            f"...parsed, {parsed.title=}, found {len(parsed.links)} links"
        )

        to_save = SavePage(path=cmd.output_path, page=parsed)
        await workflow.execute_activity(
            save_page,
            to_save,
            schedule_to_close_timeout=timedelta(seconds=5),
        )
        return OutputStats(
            url=cmd.url,
            title=parsed.title,
            nb_links=len(parsed.links),
            path=cmd.output_path,
        )
