import os

def laser_choice(params):
    '''
    Selects one of the two laser lines to assign to the position list
    Args:
        pos_i: <dict> dictionary containing the file type, file path,
               modulation, velocity, x-, y- and z- initial parameters
    Returns:
        laser_string: <string> string to tell Dilase software which laser to
                      assign to a pattern position list
    '''
    laser_line = params["laser"]
    if laser_line == 10:
        laser_string = f'"ALS" "Ligne2/Laser1" '
    elif laser_line == 0.5:
        laser_string = f'"ALS" "Ligne1/Laser1" '
    return laser_string


def position_list(params):
    '''
    Builds a simple position list. Assigns a laser line, file type, file name,
    modulation, velocity, x-, y-, z- paramters. Can repeat a single design
    a number of times in any of the axes, with a modulation and velocity shift.
    Sets a single position list assigned to a single laser line. Used to repeat
    a single LWO file.
    Args:
        pos_i: <dict> dictionary containing the file type, file path,
               modulation, velocity, x-, y- and z- initial parameters
        shift_array: <array> array containing the steps in modulation,
                     velocity, x-, y- and z- position, and number of repeats
    Returns:
        position_list: <array> array of strings containing the positions of a
                       repeated pattern in the Dilase format
    '''
    position_list = []
    laser_string = laser_choice(params=params)
    position_list.append(laser_string)
    dir_path = f'{params["filepath"]}'
    file_name = f'{params["filename"]}.LWO'
    file_path = os.path.join(dir_path, file_name)
    for i in range(0, params["repeats"]+1):
        mod = round(float(params["modulation"])+(i*params["delta_mod"]), 3)
        vel = round(float(params["velocity"])+(i*params["delta_vel"]), 3)
        x_pos = round(float(params["x_initial"])+(i*params["delta_x"]), 3)
        y_pos = round(float(params["y_initial"])+(i*params["delta_y"]), 3)
        z_pos = round(float(params["z_initial"])+(i*params["delta_z"]), 3)
        position_string = ('"LWO" '
                           f'"{file_path}" '
                           f'"{mod}" '
                           f'"{vel}" '
                           f'"{x_pos}" '
                           f'"{y_pos}" '
                           f'"{z_pos}" ')
        position_list.append(position_string)
    print(f'\nPosition List:\n')
    [print(L) for L in position_list]
    return position_list


def repeat_position_list(pos_array,
                         repeat_array):
    '''
    Builds a complete position list from a repeated pattern. Typically used in
    conjuction with the position_list function. repeat_position_list takes a
    position list array and repeats the pattern in the x, y or z direction with
    a potential variation in modulation and velocity. The laser line assigned
    in the position_list function is not altered here. Used to repeat an array
    of patterns.
    Args:
        pos_array: <array> array of strings containing the positions of a
                   repeated pattern in the Dilase format
        repeat_array: <array> array containing the steps in modulation,
                      velocity, x-, y- and z- position, and number of repeats
    Returns:
        position_list: <array> array of strings containing the positions of a
                       repeated pattern in the Dilase format
    '''
    position_list = []
    [position_list.append(L) for L in pos_array]
    for i in range(0, repeat_array[5]):
        for line in pos_array:
            split = line.split(' ')
            if split[0] == '"ALS"':
                position_list.append(line)
            if split[0] == '"LWO"':
                file_type = split[0]
                file_name = f'{split[1]} {split[2]}'
                mod = round(float((split[3])[1:-1])+((i+1)*repeat_array[0]), 3)
                vel = round(float((split[4])[1:-1])+((i+1)*repeat_array[1]), 3)
                x = round(float((split[5])[1:-1])+((i+1)*repeat_array[2]), 3)
                y = round(float((split[6])[1:-1])+((i+1)*repeat_array[3]), 3)
                z = round(float((split[7])[1:-1])+((i+1)*repeat_array[4]), 3)
                new_line = (f'{file_type} '
                            f'{file_name} '
                            f'"{mod}" '
                            f'"{vel}" '
                            f'"{x}" '
                            f'"{y}" '
                            f'"{z}" ')
                position_list.append(new_line)
    print(f'\nRepeat Position List:\n')
    [print(L) for L in position_list]
    return position_list
