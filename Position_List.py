import os
import Functions.InputOutput as io
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

file_name = "Test.lwo"
laser = 10
velocity = 5
modulation = 5
x_offset = 0
y_offset = 0
z_offset = 0

repeat_patterns = 5

position_array = []

for i in range(0, repeat_patterns):
    position_string = (f'"LWO" '
                       f'"{file_name}" '
                       f'"{modulation}" '
                       f'"{velocity}" '
                       f'"{x_offset}" '
                       f'"{y_offset}" '
                       f'"{z_offset}"')
    position_array.append(position_string)


date = datetime.date(datetime.now())
output_name = f'test_file2_{date}'
output_path = os.path.join(position_list_dir,
                           f'{output_name}.xdfl')
output_file = open(f'{output_path}', 'w')
[output_file.writelines(f'{L}\n') for L in position_array]
output_file.close()
