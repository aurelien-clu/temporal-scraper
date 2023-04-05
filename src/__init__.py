# flake8: noqa
import sys

from loguru import logger

logger.remove()

_format = (
    "<level>{level:<10}</level>"
    "<yellow>{time:YYYY-MM-DD HH:mm:ss}</yellow>|"
    "<magenta>{extra}</magenta>|"
    "<blue>{function}</blue>|"
    "<level>{message}</level>"
)

logger.add(sys.stderr, format=_format, colorize=True)

__all__ = ["logger"]
