from __future__ import annotations
from typing import List, Dict, Callable, Type, TYPE_CHECKING
from blog.domain.events.PostCreated import PostCreated
from . import post_handler

if TYPE_CHECKING:
    from . import unit_of_work


def handle(event: events.Event, uow: unit_of_work.AbstractUnitOfWork):
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
}  # type: Dict[Type[events.Event], List[Callable]]
