"""
This is the journal module
"""

import os

def load(name):
    '''
    This method creates and loads a journal.

    :param name: The base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    '''

    data = []
    filename = get_full_path(name)


    if os.path.exists(filename):
        with open(filename) as foin:
            for entry in foin.readlines():
                data.append(entry.rstrip())

    #path where is the file at
    # join with filename

    # for each line in file, append to list

    #return list
    return data

# i have to open up a file and return a list

def save(name, data):
    filename = get_full_path(name)
    print("..... saving to {}".format(filename))

    with open(filename, 'w') as fout:

        for entry in data:
            fout.write(entry + '\n')


# here the list is passed to a file


def get_full_path(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename