from typing import Any, Callable, Dict, List


class Event:
    """
    Represents an event in the application.

    Attributes:
        type (str): The type of the event.
        data (Any): The data associated with the event.
    """

    def __init__(self, type: str, data: Any = None):
        """
        Initialize an event with a type and optional data.

        Args:
            type (str): The type of the event.
            data (Any, optional): The data associated with the event. Defaults to None.
        """
        self.type = type
        self.data = data


class EventBus:
    """
    A simple event bus for publishing and subscribing to events.

    Attributes:
        listeners (Dict[str, List[Callable]]): A dictionary mapping event types to their listeners.
    """

    def __init__(self):
        """Initialize the event bus with an empty dictionary of listeners."""
        self.listeners: Dict[str, List[Callable[[Event], None]]] = {}

    def subscribe(self, event_type: str, callback: Callable[[Event], None]) -> None:
        """
        Subscribe a callback function to an event type.

        Args:
            event_type (str): The type of the event to subscribe to.
            callback (Callable[[Event], None]): The function to call when the event is published.

        Example:
            >>> def handle_event(event):
            ...     print(f"Event received: {event.type}")
            >>> event_bus.subscribe("test_event", handle_event)
        """
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(callback)

    def publish(self, event: Event) -> None:
        """
        Publish an event to all subscribed listeners.

        Args:
            event (Event): The event to publish.

        Example:
            >>> event = Event("test_event", {"key": "value"})
            >>> event_bus.publish(event)
        """
        if event.type in self.listeners:
            for callback in self.listeners[event.type]:
                callback(event)
