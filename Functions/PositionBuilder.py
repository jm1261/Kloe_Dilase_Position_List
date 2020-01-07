def x_copy(pos_i,
           shift):
    '''
    Copy an object with an x-direction shift
    Args:
        pos_i: <dict> dictionary containing the file type, file
                          path, modulation, velocity, x-, y- and z- initial
                          parameters
        shift: <float/int> step between each x co-ordinate
    '''
    position_array = []
    for i in range(0, pos_i['repeat_patterns']):
        new_x_position = round(pos_i['x_initial'] + (i*shift), 3)
        position_string = (f'"LWO" '
                           f'"{pos_i["file_name"]}" '
                           f'"{pos_i["modulation"]}" '
                           f'"{pos_i["velocity"]}" '
                           f'"{new_x_position}" '
                           f'"{pos_i["y_initial"]}" '
                           f'"{pos_i["z_initial"]}" ')
        position_array.append(position_string)
    return position_array


def y_copy(pos_i,
           shift):
    '''
    Copy an object with an y-direction shift
    Args:
        pos_i: <dict> dictionary containing the file type, file
                          path, modulation, velocity, x-, y- and z- initial
                          parameters
        shift: <float/int> step between each y co-ordinate
    '''
    position_array = []
    for i in range(0, pos_i['repeat_patterns']):
        new_y_position = round(pos_i['y_initial'] + (i*shift), 3)
        position_string = (f'"LWO" '
                           f'"{pos_i["file_name"]}" '
                           f'"{pos_i["modulation"]}" '
                           f'"{pos_i["velocity"]}" '
                           f'"{pos_i["x_initial"]}" '
                           f'"{new_y_position}" '
                           f'"{pos_i["z_initial"]}" ')
        position_array.append(position_string)
    return position_array


def z_copy(pos_i,
           shift):
    '''
    Copy an object with an z-direction shift
    Args:
        pos_i: <dict> dictionary containing the file type, file
                          path, modulation, velocity, x-, y- and z- initial
                          parameters
        shift: <float/int> step between each z co-ordinate
    '''
    position_array = []
    for i in range(0, pos_i['repeat_patterns']):
        new_z_position = round(pos_i['z_initial'] + (i*shift), 3)
        position_string = (f'"LWO" '
                           f'"{pos_i["file_name"]}" '
                           f'"{pos_i["modulation"]}" '
                           f'"{pos_i["velocity"]}" '
                           f'"{pos_i["x_initial"]}" '
                           f'"{pos_i["y_initial"]}" '
                           f'"{new_z_position}" ')
        position_array.append(position_string)
    return position_array


def modulation_x_copy(pos_i,
                      x_shift,
                      mod_shift):
    '''
    Copy an object with an x-direction shift with a different modulation
    Args:
        pos_i: <dict> dictionary containing the file type, file
                          path, modulation, velocity, x-, y- and z- initial
                          parameters
        shift: <float/int> step between each x co-ordinate
    '''
    position_array = []
    for i in range(0, pos_i['repeat_patterns']):
        new_x_position = round(pos_i['x_initial'] + (i*x_shift), 3)
        new_modulation = round(pos_i['modulation'] + (i*mod_shift), 1)
        position_string = (f'"LWO" '
                           f'"{pos_i["file_name"]}" '
                           f'"{new_modulation}" '
                           f'"{pos_i["velocity"]}" '
                           f'"{new_x_position}" '
                           f'"{pos_i["y_initial"]}" '
                           f'"{pos_i["z_initial"]}" ')
        position_array.append(position_string)
    return position_array


def modulation_y_copy(pos_i,
                      y_shift,
                      mod_shift):
    '''
    Copy an object with an y-direction shift with a different modulation
    Args:
        pos_i: <dict> dictionary containing the file type, file
                          path, modulation, velocity, x-, y- and z- initial
                          parameters
        shift: <float/int> step between each x co-ordinate
    '''
    position_array = []
    for i in range(0, pos_i['repeat_patterns']):
        new_y_position = round(pos_i['y_initial'] + (i*y_shift), 3)
        new_modulation = round(pos_i['modulation'] + (i*mod_shift), 1)
        position_string = (f'"LWO" '
                           f'"{pos_i["file_name"]}" '
                           f'"{new_modulation}" '
                           f'"{pos_i["velocity"]}" '
                           f'"{pos_i["x_initial"]}" '
                           f'"{new_y_position}" '
                           f'"{pos_i["z_initial"]}" ')
        position_array.append(position_string)
    return position_array


def modulation_z_copy(pos_i,
                      z_shift,
                      mod_shift):
    '''
    Copy an object with an z-direction shift with a different modulation
    Args:
        pos_i: <dict> dictionary containing the file type, file
                          path, modulation, velocity, x-, y- and z- initial
                          parameters
        shift: <float/int> step between each x co-ordinate
    '''
    position_array = []
    for i in range(0, pos_i['repeat_patterns']):
        new_z_position = round(pos_i['z_initial'] + (i*z_shift), 3)
        new_modulation = round(pos_i['modulation'] + (i*mod_shift), 1)
        position_string = (f'"LWO" '
                           f'"{pos_i["file_name"]}" '
                           f'"{new_modulation}" '
                           f'"{pos_i["velocity"]}" '
                           f'"{pos_i["x_initial"]}" '
                           f'"{pos_i["y_initial"]}" '
                           f'"{new_z_position}" ')
        position_array.append(position_string)
    return position_array


def velocity_x_copy(pos_i,
                    x_shift,
                    vel_shift):
    '''
    Copy an object with an x-direction shift with a different modulation
    Args:
        pos_i: <dict> dictionary containing the file type, file
                          path, modulation, velocity, x-, y- and z- initial
                          parameters
        shift: <float/int> step between each x co-ordinate
    '''
    position_array = []
    for i in range(0, pos_i['repeat_patterns']):
        new_x_position = round(pos_i['x_initial'] + (i*x_shift), 3)
        new_velocity = round(pos_i['velocity'] + (i*vel_shift), 1)
        position_string = (f'"LWO" '
                           f'"{pos_i["file_name"]}" '
                           f'"{pos_i["modulation"]}" '
                           f'"{new_velocity}" '
                           f'"{new_x_position}" '
                           f'"{pos_i["y_initial"]}" '
                           f'"{pos_i["z_initial"]}" ')
        position_array.append(position_string)
    return position_array


def velocity_y_copy(pos_i,
                    y_shift,
                    vel_shift):
    '''
    Copy an object with an y-direction shift with a different modulation
    Args:
        pos_i: <dict> dictionary containing the file type, file
                          path, modulation, velocity, x-, y- and z- initial
                          parameters
        shift: <float/int> step between each x co-ordinate
    '''
    position_array = []
    for i in range(0, pos_i['repeat_patterns']):
        new_y_position = round(pos_i['y_initial'] + (i*y_shift), 3)
        new_velocity = round(pos_i['velocity'] + (i*vel_shift), 1)
        position_string = (f'"LWO" '
                           f'"{pos_i["file_name"]}" '
                           f'"{pos_i["modulation"]}" '
                           f'"{new_velocity}" '
                           f'"{pos_i["x_initial"]}" '
                           f'"{new_y_position}" '
                           f'"{pos_i["z_initial"]}" ')
        position_array.append(position_string)
    return position_array


def velocity_z_copy(pos_i,
                    z_shift,
                    vel_shift):
    '''
    Copy an object with an z-direction shift with a different modulation
    Args:
        pos_i: <dict> dictionary containing the file type, file
                          path, modulation, velocity, x-, y- and z- initial
                          parameters
        shift: <float/int> step between each x co-ordinate
    '''
    position_array = []
    for i in range(0, pos_i['repeat_patterns']):
        new_z_position = round(pos_i['z_initial'] + (i*z_shift), 3)
        new_velocity = round(pos_i['velocity'] + (i*vel_shift), 1)
        position_string = (f'"LWO" '
                           f'"{pos_i["file_name"]}" '
                           f'"{pos_i["modulation"]}" '
                           f'"{new_velocity}" '
                           f'"{pos_i["x_initial"]}" '
                           f'"{pos_i["y_initial"]}" '
                           f'"{new_z_position}" ')
        position_array.append(position_string)
    return position_array
