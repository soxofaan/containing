# Containing

pytest helper for asserting that a container (e.g. a dict, a list, ...)
contains expected items.

Usage example:

```python
from containing import dict_containing

# Somewhere in your pytest powered test suite:
actual = {
    "size": 3,
    "color": "green",
    "shape": "triangle",
    "date": "2022-05-07",
}

# Will pass:
assert actual == dict_containing({"size": 3, "shape": "triangle"})

# Will fail:
assert actual == dict_containing({"color": "blue"})
```


## Installation

TODO (once published on PyPI: `pip install containing`)


## Why? (aka "Features")

In its simplest form, usage of something like `dict_containing`
looks like overkill. For example, the following two statements
are equivalent:

```python
assert actual["color"] == "green"
assert actual == dict_containing({"color": "green"})
```

However, once you want to check more complex situations 
(e.g. multiple keys or nested structures), 
`containing` will make things a lot easier.


