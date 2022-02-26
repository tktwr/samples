import bpy
import os
import math


def find_obj_by_name(name, data_type=bpy.types.Mesh):
    for o in bpy.data.objects:
        if o.name == name and isinstance(o.data, data_type):
            return o
    return None


def f_hide_lights():
    for o in bpy.data.objects:
        if o.name.startswith('Light'):
            o.hide_render = True


def f_show_lights(light_names):
    f_hide_lights()
    for i in light_names:
        bpy.data.objects[i].hide_render = False


def f_render(cam_name, light_names, env_file, env_intensity, rot_deg, out_file):
    bpy.context.scene.camera = bpy.context.scene.objects.get(cam_name)
    f_show_lights(light_names)
    if env_file != "":
        bpy.data.worlds["World"].node_tree.nodes['Environment Texture'].image = bpy.data.images.load(env_file)
    bpy.data.worlds["World"].node_tree.nodes['Background'].inputs[1].default_value = env_intensity
    bpy.data.worlds["World"].node_tree.nodes['Mapping'].inputs[2].default_value[2] = rot_deg * math.pi / 180

    bpy.ops.render.render()
    bpy.data.images['Render Result'].save_render(filepath = out_file)


def f_render_all(engine):
    bpy.context.scene.render.resolution_x = 512
    bpy.context.scene.render.resolution_y = 512
    bpy.context.scene.render.resolution_percentage = 100

    proj_dir = os.environ['PWD'].replace('/c/', 'C:/')
    data_dir = os.environ['MY_DATA'].replace('/c/', 'C:/')
    env_dir = f'{data_dir}/env/2k_hdr'

    if engine == 'eevee':
        output_dir = f'{proj_dir}/_output/eevee'
        bpy.context.scene.render.engine = 'BLENDER_EEVEE'
    elif engine == 'cycles':
        output_dir = f'{proj_dir}/_output/cycles'
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.device = 'GPU'

    print(f'proj_dir   = {proj_dir}')
    print(f'env_dir    = {env_dir}')
    print(f'output_dir = {output_dir}')

    render_args = (
        ('Camera_0' , ['Light_0'] , f'{env_dir}/mossy_forest_2k.hdr'    , 1 , 0 , f'{output_dir}/env_forest.png')   ,
        ('Camera_0' , ['Light_0'] , f'{env_dir}/photo_studio_01_2k.hdr' , 1 , 0 , f'{output_dir}/env_photo.png')    ,
        ('Camera_0' , ['Light_0'] , f'{env_dir}/snowy_park_01_2k.hdr'   , 1 , 0 , f'{output_dir}/env_snowy.png')    ,
        ('Camera_0' , ['Light_0'] , f'{env_dir}/studio_small_01_2k.hdr' , 1 , 0 , f'{output_dir}/env_studio01.png') ,
        ('Camera_0' , ['Light_0'] , f'{env_dir}/studio_small_07_2k.hdr' , 1 , 0 , f'{output_dir}/env_studio07.png') ,
        ('Camera_0' , ['Light_0'] , f'{env_dir}/venice_dawn_2_2k.hdr'   , 1 , 0 , f'{output_dir}/env_venice.png')   ,
        ('Camera_0' , ['Light_0'] , f''                                 , 0 , 0 , f'{output_dir}/plight.png')       ,
    )

    for i in render_args:
        f_render(*i)


f_render_all('eevee')
f_render_all('cycles')

