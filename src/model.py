import typing as t
from dataclasses import dataclass


@dataclass
class CrawlUrl:
    id: str
    url: str
    sep: str
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
    path: str
    page: ParsedPage


@dataclass
class Output:
    url: str
    title: str
    nb_links: int
    path: str
