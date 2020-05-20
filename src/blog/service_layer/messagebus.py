from __future__ import annotations
from typing import List, Dict, Callable, Type, TYPE_CHECKING
from blog.domain.events.Event import Event
from blog.domain.events.PostCreated import PostCreated
from blog.domain.events.UserCreated import UserCreated
from . import post_handler
from . import user_handler

if TYPE_CHECKING:
    from . import unit_of_work


def handle(event: Event, uow: unit_of_work.AbstractUnitOfWork):
    results = []
    queue = [event]
    while queue:
        event = queue.pop(0)
        for handler in HANDLERS[type(event)]:
            results.append(handler(event, uow=uow))
            queue.extend(uow.collect_new_events())
    return results


HANDLERS = {
    PostCreated: [post_handler.add_post],
    UserCreated: [user_handler.add_user],
}  # type: Dict[Type[events.Event], List[Callable]]
