Implement Event Observer Registry in Python

```python
from events import Events

def click_handler(note):
    print(f"clicked as '{note}'")

events = Events()
events.onclick += click_handler
events.onclick('Hi there')
```
