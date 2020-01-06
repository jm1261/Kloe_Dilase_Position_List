def x_copy(position_initial,
           shift):
    '''
    Copy an object with an x-direction shift
    Args:
        position_initial: <dict> dictionary containing the file type, file
                          path, modulation, velocity, x-, y- and z- initial
                          parameters
        shift: <float/int> step between each x co-ordinate
    '''
    position_array = []
    for i in range(0, position_initial['repeat_patterns']):
        new_x_position = round(position_initial['x_initial'] + (i*shift), 3)
        position_string = (f'"LWO" '
                           f'"{position_initial["file_name"]}" '
                           f'"{position_initial["modulation"]}" '
                           f'"{position_initial["velocity"]}" '
                           f'"{new_x_position}" '
                           f'"{position_initial["y_initial"]}" '
                           f'"{position_initial["z_initial"]}" ')
        position_array.append(position_string)
    return position_array


def y_copy(position_initial,
           shift):
    '''
    Copy an object with an y-direction shift
    Args:
        position_initial: <dict> dictionary containing the file type, file
                          path, modulation, velocity, x-, y- and z- initial
                          parameters
        shift: <float/int> step between each y co-ordinate
    '''
    position_array = []
    for i in range(0, position_initial['repeat_patterns']):
        new_y_position = round(position_initial['y_initial'] + (i*shift), 3)
        position_string = (f'"LWO" '
                           f'"{position_initial["file_name"]}" '
                           f'"{position_initial["modulation"]}" '
                           f'"{position_initial["velocity"]}" '
                           f'"{position_initial["x_initial"]}" '
                           f'"{new_y_position}" '
                           f'"{position_initial["z_initial"]}" ')
        position_array.append(position_string)
    return position_array


def z_copy(position_initial,
           shift):
    '''
    Copy an object with an z-direction shift
    Args:
        position_initial: <dict> dictionary containing the file type, file
                          path, modulation, velocity, x-, y- and z- initial
                          parameters
        shift: <float/int> step between each z co-ordinate
    '''
    position_array = []
    for i in range(0, position_initial['repeat_patterns']):
        new_z_position = round(position_initial['z_initial'] + (i*shift), 3)
        position_string = (f'"LWO" '
                           f'"{position_initial["file_name"]}" '
                           f'"{position_initial["modulation"]}" '
                           f'"{position_initial["velocity"]}" '
                           f'"{position_initial["x_initial"]}" '
                           f'"{position_initial["y_initial"]}" '
                           f'"{new_z_position}" ')
        position_array.append(position_string)
    return position_array
