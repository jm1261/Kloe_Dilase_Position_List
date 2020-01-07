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

## Firstly, what should a Kloe Dilase 650 position list look like? ##
## "ALS" "Ligne2/Laser1" ##
## "LWO" "File Name" "Modulation" "Velocity" "x-offset" "y-offset" "z-offset" ##

position_initial = {'file_name' : 'Test.lwo',
                    'laser' : 0.5,
                    'modulation' : 5,
                    'velocity' : 5,
                    'x_initial' : 0,
                    'y_initial' : 0,
                    'z_initial' : 0,
                    'repeat_patterns' : 5,
                    }

position_array = pb.velocity_x_copy(pos_i=position_initial,
                                    x_shift=0.15,
                                    vel_shift=10)

date = datetime.date(datetime.now())
output_name = f'test_file7_{date}'
output_path = os.path.join(position_list_dir,
                           f'{output_name}.xdfl')
io.write_out_file(out_path=output_path,
                  array=position_array)
