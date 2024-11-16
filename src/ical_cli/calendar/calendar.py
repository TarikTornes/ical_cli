# src/ical_cli/calendar/calendar.py
from typing import Dict, List
# from .event import Event

class Calendar:
    """Manages a collection of calendar events."""
    def __init__(self):
        self._events: Dict[str, Event] = {}

    def add_event(self, event: Event) -> None:
        """Add an event to the calendar."""
        self._events[event.uid] = event

    def remove_event(self, uid: str) -> None:
        """Remove an event from the calendar."""
        if uid in self._events:
            del self._events[uid]

    def get_event(self, uid: str) -> Event:
        """Get an event by its UID."""
        return self._events[uid]

    def list_events(self) -> List[Event]:
        """List all events in the calendar."""
        return list(self._events.values())
