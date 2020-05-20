from blog.domain.events.Event import Event
from dataclasses import dataclass
from datetime import date


@dataclass
class UserCreated(Event):
    user_id: str
    first_name: str
    last_name: str
    role: str
    created_at: date
