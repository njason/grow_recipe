from io import StringIO

import pytest
from lxml.etree import XMLSyntaxError

from grow_recipe import check_for_error


def test_basic():
    xml1 = StringIO(
        '''
        <recipe>
        </recipe>
        '''
    )
    assert not check_for_error(xml1, raise_exception=False)

    # empty buffer is not valid
    xml2 = StringIO('')

    # bug in lxml?
    assert check_for_error(xml2, raise_exception=False) in (
        'Error parsing XML',  # macOS (exception msg is None)
        "line 1: b'Document is empty'" # Ubuntu
    )

    with pytest.raises(XMLSyntaxError):
        check_for_error(xml2)
