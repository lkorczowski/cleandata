import pytest
from transform.unstructured import replace_str

def test_replace_str():
    string = "lol1, lol2, lol, lol3"
    dict_keywords = {"lol":"",
                     " ,": ""}
    assert replace_str(string, dict_keywords=dict_keywords) == "1, 2, 3"