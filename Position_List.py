import os
import Functions.InputOutput as io
import Functions.PositionBuilder as pb
from datetime import datetime

root = os.getcwd()
position_list_dir = os.path.join(root,
                                 '..',
                                 '..',
                                 'Kloe')
io.check_dir_exists(position_list_dir)

# Name of the LWO file containing your pattern (single shape or design) ##
lwo_file_name = 'Test.lwo'

# Specific system file path, Windows requires the driver to be specified ##
# as well as the file path. Dilase requires the entire path to file ##
kloe_user = 'Test'
file_name = os.path.join('D:\\',
                         'LITHO FILES',
                         f'{kloe_user}',
                         f'{lwo_file_name}')

# Firstly, what should a Kloe Dilase 650 position list look like? ##
# "ALS" "Ligne2/Laser1" ##
# "LWO" "File Name" "Modulation" "Velocity" "x-offset" "y-offset" "z-offset" ##

position_initial = {'file_name': f'{file_name}',
                    'laser': 0.5,
                    'modulation': 0.0,
                    'velocity': 0.0,
                    'x_initial': 1,
                    'y_initial': 1,
                    'z_initial': 5.359,
                    }

# pattern_shift = [modulation, velocity, x, y, z, repeats] ##
# NOTE WELL, if repeat=0 only the initial settings are set ##
# repeat=1 yields two patterns with step sizes given below ##
pattern_shift = [10, 0, 0.27, 0, 0, 10]
position_list = pb.position_list(pos_i=position_initial,
                                 shift_array=pattern_shift)

# pattern_repeat = [modulation, velocity, x, y, z, repeats] ##
# NOTE WELL, if repeat=0 only the initial settings are set  ##
# repeat=1 yields two patterns with step sizes given below  ##
pattern_repeat = [0, 10, 0, 0.15, 0, 10]
position_final = pb.repeat_position_list(pos_array=position_list,
                                         repeat_array=pattern_repeat)

z_repeat = [0, 0, 0, 0, 0.002, 10]
z_position_final = pb.repeat_position_list(pos_array=position_final,
                                           repeat_array=z_repeat)

date = datetime.date(datetime.now())
output_name = f'single_line_0-5umline_dosetest_{date}'
output_path = os.path.join(position_list_dir,
                           f'{output_name}.xdfl')
io.write_out_file(out_path=output_path,
                  array=z_position_final)
