# TODO add as button in GUI, and add shortcut
import bpy
import os # for get filepath in operation system
import datetime # for generate timestamp


get_timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
generate_filename = "\\" + get_timestamp + ".blend"
get_filepath = os.path.dirname(bpy.data.filepath)
generate_filepath = get_filepath + generate_filename

# generate new file (inactive copy)
bpy.ops.wm.save_as_mainfile(filepath = generate_filepath, copy=True)

# reference_1 https://stackoverflow.com/questions/50368143/create-unique-id-based-on-date-in-python
# reference_2: https://blender.stackexchange.com/questions/40436/add-prefix-to-filename-on-save-blender-file
