import os
import bpy


bl_info = {
    "name": "HumanTexturePanel",
    "author": "Takehiro Tawara",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "human texture panel",
    "warning": "",
    "support": "TESTING",
    "doc_url": "",
    "tracker_url": "",
    "category": "Material"
}


def f_info():
    print(f"CWD: {os.getcwd()}")
    print(bpy.data.objects)
    print(bpy.data.materials)
    print(bpy.data.textures)


def f_load_texture(mtl_name, img_fname):
    dir = f"{os.getcwd()}\\textures"
    name, ext = img_fname.split('.')
    fname = f"{dir}\\{img_fname}"
    fname_beauty = f"{dir}\\{name}_beauty.{ext}"
    print(fname)
    print(fname_beauty)
    img = bpy.data.images.load(fname)
    img_beauty = bpy.data.images.load(fname_beauty)

    nodes = bpy.data.materials[mtl_name].node_tree.nodes
    for i in nodes:
        print(i)
    nodes["Image Texture"].image = img
    nodes["Image Texture.001"].image = img_beauty


class MY_OT_next_btn(bpy.types.Operator):
    bl_label = "Next"
    bl_idname = "my.next_btn"
    idx = 0
    size = 2

    def execute(self, context):
        idx = MY_OT_next_btn.idx
        size = MY_OT_next_btn.size

        #f_info()

        fname = f"Head_diffuse_{idx+1:02}.png"
        f_load_texture("Head_skin_edit", fname)
        idx += 1
        idx = idx % size
        MY_OT_next_btn.idx = idx
        return {'FINISHED'}


class MY_PT_ui(bpy.types.Panel):
    bl_label = "Human Texture"
    bl_category = "Human Texture"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        skin_color = bpy.data.materials["Head_skin_edit"].node_tree.nodes["RGB"].outputs[0]
        row.prop(skin_color, "default_value", text="Skin Color")

        row = layout.row()
        beauty_val = bpy.data.materials["Head_skin_edit"].node_tree.nodes["Mix"].inputs[0]
        row.prop(beauty_val, "default_value", text="Beauty", slider=True)

        row = layout.row()
        row.operator("my.next_btn")

        row = layout.row()
        row.operator("render.render")


classes = (
    MY_PT_ui,
    MY_OT_next_btn
)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()

