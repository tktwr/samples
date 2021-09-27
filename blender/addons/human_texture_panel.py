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


class MY_OT_button(bpy.types.Operator):
    bl_label = "text"
    bl_idname = "my.button"

    def execute(self, context):
        print("pushed")
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
        row.operator("my.button")

        row = layout.row()
        row.operator("render.render")


classes = (
    MY_PT_ui,
    MY_OT_button
)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()

