from datetime import timedelta

from temporalio import workflow

# Import our activity, passing it through the sandbox
with workflow.unsafe.imports_passed_through():
    from activities import fetch_page, parse_page, save_page
    from model import CrawlUrl, FetchedPage, Output, ParsedPage, SavePage


@workflow.defn
class CrawlWebsite:
    @workflow.run
    async def run(self, cmd: CrawlUrl) -> Output:
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
        path = cmd.output_dir + cmd.sep + f"{cmd.id}.json"
        to_save = SavePage(path=path, page=parsed)
        await workflow.execute_activity(
            save_page,
            to_save,
            schedule_to_close_timeout=timedelta(seconds=5),
        )

        return Output(
            url=cmd.url,
            title=parsed.title,
            nb_links=len(parsed.links),
            path=to_save.path,
        )
