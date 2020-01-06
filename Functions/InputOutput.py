import os


def check_dir_exists(dir_path):
    '''
    Check to see if a directory path exists, and if not create one
    Args:
        dir_path: <string> directory path
    '''
    if os.path.isdir(dir_path) is False:
        os.mkdir(dir_path)


def write_out_file(out_path,
                   array):
    '''
    Writes a simpled text file, txt or other extension, based on a given array
    containing strings. The array entries are written on each line.
    Args:
        out_path: <string> directory path to write file
        array: <array> array containing the out file strings
    '''
    output_file = open(f'{out_path}', 'w')
    [output_file.writelines(f'{L}\n') for L in array]
    output_file.close()
