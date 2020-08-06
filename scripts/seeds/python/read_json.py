import sys
import json
import codecs

def get_ops():
    try:
        with codecs.open('ops.json', 'r', encoding='utf-8') as fh:
            txt = json.loads(fh)
    except IOError:
        raise TypeError("Error reading file: {}".format(filename))

    return txt


get_ops()