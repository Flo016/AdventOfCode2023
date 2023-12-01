

def get_clean_file_input(filepath: str):
    """
    Gets the cleaned lines of an input file cleaned
    :param filepath:
    :return: The lines of the file as an array without newline characters
    """
    return [line.replace("\n", "") for line in open(filepath).readlines()]
