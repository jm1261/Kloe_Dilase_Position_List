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
                   array,
                   pos_i):
    '''
    Writes a simpled text file, txt or other extension, based on a given array
    containing strings. The array entries are written on each line.
    Args:
        out_path: <string> directory path to write file
        array: <array> array containing the out file strings
    '''
    laser_line = pos_i['laser']
    if laser_line == 10:
        laser_string = f'"ALS" "Ligne2/Laser1" '
    elif laser_line == 0.5:
        laser_string = f'"ALS" "Ligne1/Laser1" '
    output_file = open(f'{out_path}', 'w')
    output_file.writelines('"DflVersion" "3"\n')
    output_file.writelines(f'{laser_string}\n')
    [output_file.writelines(f'{L}\n') for L in array]
    output_file.close()
