from blog.domain.events.Event import Event
from dataclasses import dataclass
from datetime import date


@dataclass
class PostCreated(Event):
    post_id: str
    user_id: str
    title: str
    body: str
    created_at: date
