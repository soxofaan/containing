from containing import dict_containing


def test_dict_containing_empty():
    assert {} == dict_containing()
    assert {1: 2} == dict_containing()
    assert {"foo": "bar"} == dict_containing()

    assert not ([] == dict_containing())
    assert not (() == dict_containing())
    assert not (set([]) == dict_containing())


def test_dict_containing_basic():
    d = {"size": 3, "color": "green"}
    assert d == dict_containing()
    assert d == dict_containing({"size": 3})
    assert d == dict_containing({"color": "green"})
    assert d == dict_containing({"size": 3, "color": "green"})
    assert not (d == dict_containing({"size": 33, "color": "green"}))
    assert not (d == dict_containing({"size": 3, "color": "red"}))


def test_dict_containing_kwargs():
    d = {"size": 3, "color": "green"}
    assert d == dict_containing(size=3)
    assert d == dict_containing(size=3, color="green")
    assert d == dict_containing({"size": 3}, color="green")
    assert not (d == dict_containing(size=4))
    assert not (d == dict_containing(color="red"))


def test_dict_containing_other_key_types():
    d = {"color": "green", 22: 333, ("Bob", "Alice"): "married"}
    assert d == dict_containing({22: 333})
    assert d == dict_containing({("Bob", "Alice"): "married"})
