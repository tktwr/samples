import bpy
import os


def f_render_env(env_file, out_file):
    bpy.context.scene.world.node_tree.nodes['Environment Texture'].image = bpy.data.images.load(env_file)
    bpy.ops.render.render()
    bpy.data.images['Render Result'].save_render(filepath = out_file)


proj_dir = os.environ['PWD'].replace('/c/', 'C:/')

env_file = f"{proj_dir}/env/2k_hdr/studio_small_07_2k.hdr"
out_file = f"{proj_dir}/cy_env_studio07.png"
f_render_env(env_file, out_file)

env_file = f"{proj_dir}/env/2k_hdr/venice_dawn_2_2k.hdr"
out_file = f"{proj_dir}/cy_env_venice.png"
f_render_env(env_file, out_file)

