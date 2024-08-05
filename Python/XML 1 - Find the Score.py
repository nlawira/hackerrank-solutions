import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    res = len(node.attrib)
    if len(node):
        for tag in node:
            res += get_attr_number(tag)
    return res

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))