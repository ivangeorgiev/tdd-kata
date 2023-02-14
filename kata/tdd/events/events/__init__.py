class EventsException(Exception):
    pass

class EventNotDeclared(EventsException):
    pass

class EventSlot:
    def __init__(self):
        self.targets = []

    def __call__(self, *args, **kwargs):
        for target in self.targets:
            try:
                target(*args, **kwargs)
            except:
                pass

    def __iadd__(self, target):
        self.targets.append(target)
        return self
    
    def __isub__(self, target):
        while target in self.targets:
            self.targets.remove(target)
        return self


class Events:
    def __init__(self, event_names=None, event_slot_factory=None):
        if event_names:
            self._event_names = event_names[:]
        self._event_slot_factory = event_slot_factory or EventSlot

    def __getattr__(self, name):
        if name.startswith("_"):
            raise AttributeError(
                "'{}' object has no attribute '{}'".format(type(self).__qualname__, name)
            )
        
        if hasattr(self, '_event_names'):
            if name not in self._event_names:
                raise EventNotDeclared(f"Event '{name}' is not declared")

        self.__dict__[name] = event_slot = self._event_slot_factory()
        return event_slot
