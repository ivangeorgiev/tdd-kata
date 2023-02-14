from unittest.mock import Mock
from events import Events, EventSlot, EventNotDeclared
import pytest

class TestEventsClass:
    def test_initializer_should_set_defaults(self):
        events = Events()
        assert not hasattr(events, "_event_names")
        assert events._event_slot_factory is EventSlot

    def test_initializer_should_set_properties(self):
        def event_slot_factory():
            pass
        event_names = ['onchange']
        events = Events(event_names, event_slot_factory)
        assert events._event_names == event_names
        assert events._event_names is not event_names
        assert events._event_slot_factory is event_slot_factory

    def test_gettattr_should_call_event_slot_factory_to_create_attribute_and_return_result(self):
        event_slot_factory = Mock()
        events = Events(event_slot_factory=event_slot_factory)
        slot = events.onevent
        assert slot is event_slot_factory.return_value
        assert hasattr(events, 'onevent')

    def test_getattr_should_raise_AttributeError_when_attribute_name_starts_with_underline(self):
        events = Events()
        with pytest.raises(AttributeError, match="'Events' object has no attribute '_onevent'"):
            events._onevent

    def test_getattr_should_raise_EventNotDeclared_when_event_name_is_not_in_event_names(self):
        events = Events(['declared'])
        with pytest.raises(EventNotDeclared, match="Event 'not_declared' is not declared"):
            events.not_declared

    def test_event_names_could_be_registered_in_subclass_attribute(self):
        class SomeEvents(Events):
            _event_names = ['onclick']

        events = SomeEvents()

        with pytest.raises(EventNotDeclared):
            events.not_declared
        events.onclick

class TestEventSlotClass:

    def test_initializer_should_set_defaults(self):
        slot = EventSlot()
        assert slot.targets == []

    def test_increment_should_append_target(self):
        slot = EventSlot()
        target = Mock()
        slot += target
        assert slot.targets == [target]

    def test_decrement_should_remove_target(self):
        slot = EventSlot()
        target = Mock()
        slot.targets.append(target)
        slot -= target
        assert not slot.targets

    def test_call_should_call_targets_passing_arguments(self):
        slot = EventSlot()
        target = Mock()
        slot.targets.append(target)
        args = [1,2]
        kwargs = {"a":"b", "c": "d"}
        slot(*args, **kwargs)
        target.assert_called_once_with(*args, **kwargs)

    def test_call_should_not_raise_exception_from_target(self):
        slot = EventSlot()
        target = Mock()
        target.side_effect = Exception("you will never see me")
        slot.targets.append(target)
        slot()
