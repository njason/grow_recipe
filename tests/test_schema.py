from io import StringIO

import pytest

LXML_INSTALLED = True
try:
    from lxml.etree import XMLSyntaxError
except ModuleNotFoundError:
    LXML_INSTALLED = False

from grow_recipe import check_for_error


def test_basic():

    if not LXML_INSTALLED:
        pytest.skip('lxml package needs to be installed')

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
