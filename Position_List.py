import os
import Functions.InputOutput as io
import Functions.PositionBuilder as pb
from datetime import datetime
import Functions.BuildForm as bf

root = os.getcwd()
position_list_dir = os.path.join(root,
                                 '..',
                                 '..',
                                 'Kloe')
io.check_dir_exists(position_list_dir)

fields_path = os.path.join(root, 'Fields.config')
fields_dict = io.get_config(config_path=fields_path)
fields = [key for key in fields_dict]
bf.make_window(fields=fields)

config_path = os.path.join(root, 'Params.config')
params = io.get_config(config_path=config_path)

position_list = pb.position_list(params=params)
print(position_list)


# # pattern_repeat = [modulation, velocity, x, y, z, repeats] ##
# # NOTE WELL, if repeat=0 only the initial settings are set  ##
# # repeat=1 yields two patterns with step sizes given below  ##
# position_final = pb.repeat_position_list(pos_array=position_list,
#                                          repeat_array=pattern_repeat)
#
# date = datetime.date(datetime.now())
# output_name = f'single_line_0-5umline_dosetest_{date}'
# output_path = os.path.join(position_list_dir,
#                            f'{output_name}.xdfl')
# io.write_out_file(out_path=output_path,
#                   array=z_position_final)
