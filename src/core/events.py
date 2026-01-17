# events.py
class Event:
    def __init__(self, type, data=None):
        self.type = type
        self.data = data


class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, callback):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(callback)

    def publish(self, event):
        if event.type in self.listeners:
            for callback in self.listeners[event.type]:
                callback(event)
