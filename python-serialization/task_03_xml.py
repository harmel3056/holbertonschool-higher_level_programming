#!/usr/bin/python3
"""
Demonstration of serialization and deserialization using XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to XML

    Args:
    dictionary - Python dictionary to serialize to XML
    filename - name to give the output file

    Return:
    None, but writes the output to a new XML file
    """
    root = ET.Element("data")
    # creates a new root element

    for key, value in dictionary.items():
        # loops and increments through dict
        child = ET.SubElement(root, key)
        # creates sub-nodes for every key
        child.text = str(value)
        # assigns values to sub-nodes, which must be in string format

    tree = ET.ElementTree(root)
    # wraps data from root in an ElementTree object for data navigation
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    # writes the data to filename


def deserialize_from_xml(filename):
    """
    Deserializes an XML back to Python dictionary

    Args:
    filename - name of the file to deserialize

    Return:
    Python dictionary
    """
    tree = ET.parse(filename)
    # takes the file name as an argument and returns an ElementTree object
    root = tree.getroot()
    # accesses the root as an access point for remainder of file
    dictionary = {}
    # creates a placeholder dictionary

    for child in root:
        dictionary[child.tag] = child.text
        # assigns XML tag as key and text as value

    return dictionary
