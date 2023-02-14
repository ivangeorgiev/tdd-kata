# Event Observer Registry in Python

## Usage

Use `Events` class as observer registry. To add observer to an event, use the `+=` operator.

```python
from events import Events

def click_handler(note):
    print(f"clicked as '{note}'")

events = Events()
events.onclick += click_handler
events.onclick('Hi there')
```
