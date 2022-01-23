import bpy
import os


def f_render_env(env_file, out_file):
    bpy.context.scene.world.node_tree.nodes['Environment Texture'].image = bpy.data.images.load(env_file)
    bpy.ops.render.render()
    bpy.data.images['Render Result'].save_render(filepath = out_file)


def f_render_all(engine):
    bpy.context.scene.render.resolution_x = 512
    bpy.context.scene.render.resolution_y = 512

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

    env_files = (
        (f'{env_dir}/mossy_forest_2k.hdr', f'{output_dir}/env_forest.png'),
        (f'{env_dir}/photo_studio_01_2k.hdr', f'{output_dir}/env_photo.png'),
        (f'{env_dir}/snowy_park_01_2k.hdr', f'{output_dir}/env_snowy.png'),
        (f'{env_dir}/studio_small_01_2k.hdr', f'{output_dir}/env_studio01.png'),
        (f'{env_dir}/studio_small_07_2k.hdr', f'{output_dir}/env_studio07.png'),
        (f'{env_dir}/venice_dawn_2_2k.hdr', f'{output_dir}/env_venice.png'),
    )

    for i in env_files:
        env_fname, out_fname = i
        print(f'{env_fname} {out_fname}')
        f_render_env(env_fname, out_fname)

f_render_all('eevee')
f_render_all('cycles')
