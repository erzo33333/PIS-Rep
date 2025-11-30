import pytest
from program import safe_get
from errors import FieldMissingError

def test_safe_get_ok():
    d = {"name": "яблоко", "amount": 17}
    assert safe_get(d, "name") == "яблоко"

def test_safe_get_missing():
    with pytest.raises(FieldMissingError):
        safe_get({}, "name")
