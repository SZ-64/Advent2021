def read_file_as_lines(name):
    """ Opens the specified file for reading and returns each line as a string. """
    f = open(name, "r")
    return f.read().split('\n')


def read_file_as_ints(name):
    """ Opens the specified file for reading and returns each line as an int. """
    return [int(x) for x in read_file_as_lines(name)]
