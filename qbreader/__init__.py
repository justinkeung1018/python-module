"""The official qbreader API python wrapper."""

import importlib.metadata

from qbreader.asynchronous import Async
from qbreader.synchronous import Sync
from qbreader.types import (
    AnswerJudgement,
    Bonus,
    Category,
    Difficulty,
    Directive,
    Packet,
    QueryResponse,
    Subcategory,
    Tossup,
)

__version__ = importlib.metadata.version("qbreader")
__all__ = (
    "Async",
    "Sync",
    "Tossup",
    "Bonus",
    "Category",
    "Subcategory",
    "Difficulty",
    "QueryResponse",
    "Directive",
    "AnswerJudgement",
    "Packet",
)

del importlib
