import typing as t
from dataclasses import dataclass


@dataclass
class CrawlUrl:
    url: str
    output_dir: str


@dataclass
class FetchedPage:
    url: str
    html_body: str


@dataclass
class ParsedPage:
    url: str
    title: str
    links: t.List[str]


@dataclass
class SavePage:
    output_dir: str
    page: ParsedPage
