from datetime import datetime
from typing import Optional

class Event:
    """Represents a calendar event."""

    def __init__(
        self, 
        uid: str, 
        summary: str, 
        start_time: datetime, 
        end_time: datetime, 
        description: Optional[str] = None, 
        location: Optional[str] = None
    ):
        self.uid = uid
        self.summary = summary
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.location = location

    def to_ical_format(self) -> str:
        """Convert event to iCalendar format."""
        ical_str = []
        ical_str.append("BEGIN:VEVENT")
        ical_str.append(f"UID:{self.uid}")
        ical_str.append(f"SUMMARY:{self.summary}")
        ical_str.append(f"DTSTART:{self.start_time.strftime('%Y%m%dT%H%M%SZ')}")
        ical_str.append(f"DTEND:{self.end_time.strftime('%Y%m%dT%H%M%SZ')}")
        if self.description:
            ical_str.append(f"DESCRIPTION:{self.description}")
        if self.location:
            ical_str.append(f"LOCATION:{self.location}")
        ical_str.append("END:VEVENT")
        return "\n".join(ical_str)
