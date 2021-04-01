import os
from datetime import datetime
from operator import itemgetter


def laser_choice(laser_line):
    '''
    Selects one of the two available laser lines to assign to position list.
    Args:
        laser_line: <boolean> [10/0.5] size of laser line in mircometers
    Returns:
        laser_string: <string> instruction string for position list
    '''
    if laser_line == 10:
        laser_string = f'"ALS" "Ligne2/Laser1"'
    elif laser_line == 0.5:
        laser_string = f'"ALS" "Ligne1/Laser1"'
    return laser_string


def position_list(position_dict):
    '''
    '''
    path, user, name, laser, params_i, params_d, repeats = itemgetter(
        "filepath", "user", "filename", "laser", 
        "params_initial", "params_delta", "repeats")(position_dict)
    position_list = []
    position_list.append(laser_choice(laser_line=laser))
    file_path = os.path.join(path, user, name)
    for i in range(0, repeats+1):
        mod = round(float(params_i[0]) + (i * params_d[0]), 3)
        vel = round(float(params_i[1]) + (i * params_d[1]), 3)
        x_pos = round(float(params_i[2]) + (i * params_d[2]), 3)
        y_pos = round(float(params_i[3]) + (i * params_d[3]), 3)
        z_pos = round(float(params_i[4]) + (i * params_d[4]), 3)
        pos_string = (f'"LWO" "{file_path}" "{mod}" "{vel}" '
                      f'"{x_pos}" "{y_pos}" "{z_pos}" ')
        position_list.append(pos_string)
    [print(l) for l in position_list]
    return position_list


if __name__ == '__main__':
    root = os.getcwd()
    pos_dict = {
        "filepath": "D:\\LITHO FILES",
        "user": "Josh",
        "filename": "Test.LWO",
        "laser": 10,
        "params_example": "[mod, vel, x, y, z]",
        "params_initial": [10, 10, 1, 1, 5],
        "params_delta": [10, 10, 1, 1, 0],
        "repeats": 10
    }
    pos_list = position_list(position_dict=pos_dict)
    date = datetime.date(datetime.now())
    out_name = f'Test_{date}.xdfl'
    out_path = os.path.join(root, out_name)
    output_file = open(f'{out_path}', 'w')
    output_file.writelines('"DflVersion" "3"\n')
    [output_file.writelines(f'{L}\n' for L in pos_list)]
    output_file.close()
