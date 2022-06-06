from typing import Optional, Sequence, Hashable

__all__ = ["dict_containing", "dict_having_keys"]


# TODO: chained API to combine `containing` and `having_keys`?
# TODO: helper to convert nested dict to nested `dict_containing` structure

class _DictMatcher:

    def __init__(self, containing: Optional[dict] = None, having_keys: Optional[Sequence[Hashable]] = None):
        self._containing = containing or {}
        self._having_keys = having_keys or []

    def __eq__(self, other):
        return isinstance(other, type(self._containing)) and \
               all(k in other and other[k] == v for k, v in self._containing.items()) and \
               all(k in other for k in self._having_keys)

    def __repr__(self):
        # TODO: include _having_keys in repr?
        return repr(self._containing)


def dict_containing(items: Optional[dict] = None, **kwargs):
    """
    pytest helper to assert that a dictionary at least contains given items, e.g.:

        >>> actual = {"size": 3, "color": "red"}
        >>> assert actual == dict_containing({"size": 3})
    """
    return _DictMatcher(containing={**(items or {}), **kwargs})


def dict_having_keys(*args):
    """
    pytest helper to assert that a dictionary at least contains given keys, e.g.:

        >>> actual = {"size": 3, "color": "red"}
        >>> assert actual == dict_having_keys("size")
    """

    if len(args) == 1 and isinstance(args[0], (list, set)):
        args = args[0]
    return _DictMatcher(having_keys=args)
