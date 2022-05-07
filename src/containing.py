class _DictMatcher:

    def __init__(self, containing: dict = None):
        self.containing = containing or {}

    def __eq__(self, other):
        return isinstance(other, type(self.containing)) and \
               self.containing == {k: other[k] for k in self.containing if k in other}

    def __repr__(self):
        return repr(self.containing)


def dict_containing(items: dict = None, **kwargs):
    """
    pytest helper to assert that a dictionary at least contains given items, e.g.:

        >>> assert {"size": 3, "color": "red"} == dict_containing({"size": 3})
    """
    return _DictMatcher(containing={**(items or {}), **kwargs})
