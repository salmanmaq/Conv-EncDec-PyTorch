import json

def parse_classes(filename):
    '''
        Read the classes json file to obtain the classe ids, names, and
        colors representing each class.

        Args:
            filename: The file path to the classes.json file
    '''

    with open(filename, 'r') as f:
        classes = json.load(f)
