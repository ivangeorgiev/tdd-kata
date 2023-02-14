# Event Observer Registry in Python

## Usage

### Creating event observer registry

Create `Events` class instance to create event observer registry:

```python
>>> from events import Events
>>> events = Events()
```

### Subscribing to an event

To subscribe an observer to an event, use the `+=` operator:

```python
>>> def click_handler(note):
...    print(f"clicked with note '{note}'")
... 
>>> events.onclick += click_handler
```

### Handle an event

To handle an event, call the event slot:

```python
>>> events.onclick('Hi there')
Clicked with note 'Hi there'
```
