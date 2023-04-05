from datetime import timedelta

from temporalio import workflow

# Import our activity, passing it through the sandbox
with workflow.unsafe.imports_passed_through():
    from scraper_activities import fetch_page, parse_page, save_page
    from scraper_model import CrawlUrl, FetchedPage, ParsedPage, SavePage, OutputStats


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
        workflow.logger.info(f"...{cmd.url} fetched")

        parsed: ParsedPage = await workflow.execute_activity(
            parse_page,
            page,
            schedule_to_close_timeout=timedelta(seconds=5),
        )
        workflow.logger.info(f"{cmd.url} parsed, {parsed.title=}, found {len(parsed.links)} links")

        workflow.logger.info(f"saving {cmd.url} results to {cmd.output_dir}...")
        await workflow.execute_activity(
            save_page,
            SavePage(output_dir=cmd.output_dir, page=parsed),
            schedule_to_close_timeout=timedelta(seconds=5),
        )
        workflow.logger.info("...result saved")

        return OutputStats(url=cmd.url, title=parsed.title, nb_links=len(parsed.links))
