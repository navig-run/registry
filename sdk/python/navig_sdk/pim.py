"""Calendar, email and contact types shared by navig and its standalone plugins.

``navig.agent.proactive.providers`` is an alias of this module (one copy), and
``navig.messaging.adapter`` imports :class:`Contact` / :class:`Route` from here, so a contact
read by the standalone ``navig-contacts`` IS the object navig's message routing resolves.


Proactive Assistance Providers

Interfaces for Calendar, Email, and other services that the
agent can proactively monitor and interact with.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class Route:
    """A single transport route for a contact."""

    network: str  # e.g. "whatsapp", "discord", "sms"
    address: str  # e.g. "+33612345678", "123456789"
    priority: int = 0
    meta: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Contact:
    """Resolved contact with ordered routes and fallbacks."""

    alias: str
    display_name: str
    default_network: str | None = None
    routes: list[Route] = field(default_factory=list)
    fallbacks: list[str] = field(default_factory=list)
    created_at: str = ""
    updated_at: str = ""


@dataclass
class CalendarEvent:
    id: str
    title: str
    start: datetime
    end: datetime
    location: str | None = None
    description: str | None = None
    attendees: list[str] | None = None


@dataclass
class EmailMessage:
    id: str
    subject: str
    sender: str
    snippet: str
    received_at: datetime
    read: bool = False


class CalendarProvider(ABC):
    """Abstract interface for Calendar integration."""

    @abstractmethod
    async def list_events(self, start: datetime, end: datetime) -> list[CalendarEvent]:
        """List events in range."""
        pass

    @abstractmethod
    async def create_event(self, event: CalendarEvent) -> str:
        """Create new event, return ID."""
        pass


class EmailProvider(ABC):
    """Abstract interface for Email integration."""

    @abstractmethod
    async def list_unread(self, limit: int = 10) -> list[EmailMessage]:
        """Get unread messages."""
        pass

    @abstractmethod
    async def draft_email(self, to: list[str], subject: str, body: str) -> str:
        """Create draft email, return ID."""
        pass


class MockCalendar(CalendarProvider):
    """Mock implementation for testing."""

    async def list_events(self, start: datetime, end: datetime) -> list[CalendarEvent]:
        # Return a fake meeting
        return [
            CalendarEvent(
                id="mock-1",
                title="Weekly Sync",
                start=datetime.now().replace(hour=10, minute=0),
                end=datetime.now().replace(hour=11, minute=0),
                attendees=["alice@example.com", "bob@example.com"],
            )
        ]

    async def create_event(self, event: CalendarEvent) -> str:
        print(f"[MOCK] Created event: {event.title}")
        return "mock-event-id"


class MockEmail(EmailProvider):
    """Mock implementation for testing."""

    async def list_unread(self, limit: int = 10) -> list[EmailMessage]:
        return [
            EmailMessage(
                id="msg-1",
                subject="Project Update",
                sender="boss@company.com",
                snippet="Can we deploy today?",
                received_at=datetime.now(),
            )
        ]

    async def draft_email(self, to: list[str], subject: str, body: str) -> str:
        print(f"[MOCK] Drafted email to {to}: {subject}")
        return "mock-draft-id"
