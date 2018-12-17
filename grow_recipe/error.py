"""
Validates a an XML file with an XML schema. Nothing grow recipe specific
"""
import os
from functools import wraps

from lxml import etree

DEFAULT_SCHEMA = os.path.join(os.path.dirname(__file__), 'schema/recipe.xsd')


def error(xml, schema=None, raise_exception=True):
    """
    Returns the schema error message, if there is no errors it returns None
    """

    if not schema:
        with open(DEFAULT_SCHEMA, 'r') as schema_file:
            schema_tree = etree.parse(schema_file)
            schema = etree.XMLSchema(schema_tree)

    xml_str = xml.read().replace('\n', '').encode('utf-8')
    parser = etree.XMLParser(schema=schema)

    try:
        etree.fromstring(xml_str, parser)
    except etree.XMLSyntaxError as e:
        if raise_exception:
            raise

        return e.msg

    return None
