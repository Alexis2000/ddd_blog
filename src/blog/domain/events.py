# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from datetime import date


class Event:
    pass


@dataclass
class PostCreated(Event):
    post_id: str
    user_id: str
    title: str
    body: str
    created_at: date


@dataclass
class PostCreatedByNoneAdmin(Event):
    sku: str
