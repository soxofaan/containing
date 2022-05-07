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
    assert not (d == dict_containing({"speed": 11}))


def test_dict_containing_kwargs():
    d = {"size": 3, "color": "green"}
    assert d == dict_containing(size=3)
    assert d == dict_containing(size=3, color="green")
    assert d == dict_containing({"size": 3}, color="green")
    assert not (d == dict_containing(size=4))
    assert not (d == dict_containing(color="red"))
    assert not (d == dict_containing(speed=11))


def test_dict_containing_other_key_types():
    d = {"color": "green", 22: 333, ("Bob", "Alice"): "married"}
    assert d == dict_containing({22: 333})
    assert d == dict_containing({("Bob", "Alice"): "married"})


def test_dict_containing_nesting():
    d = {
        "color": "green",
        "size": {"x": 3, "y": 5, "z": 8},
        "metadata": {
            "create": {
                "date": "2022-05-07",
                "authors": [
                    {"id": "j0hn", "name": {"first": "John", "last": "Doe"}},
                ]
            }
        }
    }
    assert d == dict_containing(
        color="green",
        size=dict_containing(x=3, y=5)
    )
    assert d == dict_containing({"metadata": {"create": dict_containing(date="2022-05-07")}})
    assert d == dict_containing({
        "metadata": {
            "create": dict_containing(
                authors=[dict_containing(id="j0hn")],
            ),
        }
    })
    assert d == dict_containing({
        "metadata": {
            "create": dict_containing(
                authors=[
                    dict_containing(name=dict_containing(last="Doe")),
                ],
            ),
        }
    })
    assert not (d == dict_containing({
        "metadata": {
            "create": dict_containing(
                authors=[
                    dict_containing(name=dict_containing(last="McSmithson-sur-Schelde")),
                ],
            ),
        }
    }))
