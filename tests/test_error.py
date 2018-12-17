from io import StringIO

import pytest
from lxml.etree import XMLSyntaxError

from grow_recipe import error


def test_basic():
    xml1 = StringIO(
        '''
        <recipe>
        </recipe>
        '''
    )
    assert not error(xml1)

    # empty buffer is not valid
    xml2 = StringIO('')
    assert error(xml2, raise_exception=False) == "line 1: b'Document is empty'"
    with pytest.raises(XMLSyntaxError):
        error(xml2)
