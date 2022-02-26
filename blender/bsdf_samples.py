import bpy
import os
import math


MAT_PARAM_30 = {
    "Base Color": 0,
    "Subsurface": 1,
    "Subsurface Radius": 2,
    "Subsurface Color": 3,
    "Subsurface IOR": 4,
    "Subsurface Anisotropy": 5,
    "Metallic": 6,
    "Specular": 7,
    "Specular Tint": 8,
    "Roughness": 9,
    "Anisotropic": 10,
    "Anisotropic Rotation": 11,
    "Sheen": 12,
    "Sheen Tint": 13,
    "Clearcoat": 14,
    "Clearcoat Roughness": 15,
    "IOR": 16,
    "Transmission": 17,
    "Transmission Roughness": 18,
    "Emission": 19,
    "Emission Strength": 20,
    "Alpha": 21,
    "Normal": 22,
    "Clearcoat Normal": 23,
    "Tangent": 24,
}


#======================================================
def radians3(deg3):
    return [math.radians(i) for i in deg3]


def clear_all():
    for i in bpy.data.cameras:
        bpy.data.cameras.remove(i)
    for i in bpy.data.lights:
        bpy.data.lights.remove(i)
    for i in bpy.data.meshes:
        bpy.data.meshes.remove(i)
    for i in bpy.data.materials:
        bpy.data.materials.remove(i)
    for i in bpy.data.objects:
        bpy.data.objects.remove(i)
    for i in bpy.data.collections:
        bpy.data.collections.remove(i)


def set_mat_custom_props():
    for mat in bpy.data.materials:
        print(f'mat.name = {mat.name}')
        bsdf = find_principled_bsdf_node(mat)
        if bsdf != None:
            print(f'bsdf.name = {bsdf.name}')
            mat['u_subsurface_radius'] = get_mat_param(mat, 'Subsurface Radius')
            mat['u_specular'] = get_mat_param(mat, 'Specular')
            mat['u_specular_tint'] = get_mat_param(mat, 'Specular Tint')
            mat['u_ior'] = get_mat_param(mat, 'IOR')
            mat['u_transmission'] = get_mat_param(mat, 'Transmission')
            mat['u_transmission_roughness'] = get_mat_param(mat, 'Transmission Roughness')


#------------------------------------------------------
# add
#------------------------------------------------------
def add_collection_to_scene(coll):
    bpy.context.scene.collection.children.link(coll)


def add_object_to_scene(obj):
    bpy.context.scene.collection.objects.link(obj)


def link_object_to_collection(obj, coll):
    coll.objects.link(obj)
    bpy.context.scene.collection.objects.unlink(obj)


#------------------------------------------------------
# create
#------------------------------------------------------
def create_collection(name):
    return bpy.data.collections.new(name)


def create_camera(name, loc, rot_deg):
    data = bpy.data.cameras.new(name=name)
    obj = bpy.data.objects.new(name, data)
    obj.location = loc
    obj.rotation_euler = radians3(rot_deg)
    return obj


def create_light(name, loc, power):
    data = bpy.data.lights.new(name=name, type='POINT')
    data.energy = power
    obj = bpy.data.objects.new(name=name, object_data=data)
    obj.location = loc
    return obj


def create_sphere(name, radius, loc):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=loc, scale=(1, 1, 1))
    bpy.ops.object.shade_smooth()
    obj = bpy.context.view_layer.objects.active
    obj.name = name
    obj.data.name = name
    return obj


def create_material(name):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    return mat


#------------------------------------------------------
# material
#------------------------------------------------------
def find_principled_bsdf_node(mat):
    if mat.node_tree != None:
        for i in mat.node_tree.nodes:
            if i.name.startswith('Principled BSDF') or i.name.startswith('プリンシプルBSDF'):
                return i
    return None


def set_obj_material(obj, mat):
    obj_matslots = obj.material_slots
    if len(obj_matslots) == 0:
        obj.data.materials.append(mat)
    else:
        obj_matslots[obj.active_material_index].material = mat


def set_mat_param(mat, mat_param_name, val):
    #bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf = find_principled_bsdf_node(mat)
    mat_param_id = MAT_PARAM_30[mat_param_name]
    bsdf.inputs[mat_param_id].default_value = val


def get_mat_param(mat, mat_param_name):
    #bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf = find_principled_bsdf_node(mat)
    mat_param_id = MAT_PARAM_30[mat_param_name]
    return bsdf.inputs[mat_param_id].default_value


#======================================================
# main
#======================================================
MAT_BLENDER_DEFAULT = {
    "Base Color": (0.8, 0.8, 0.8, 1.0),
    "Subsurface": 0.0,
    "Subsurface Radius": (1.0, 0.2, 0.1),
    "Subsurface Color": (0.8, 0.8, 0.8, 1.0),
    "Subsurface IOR": 1.4,
    "Subsurface Anisotropy": 0.0,
    "Metallic": 0.0,
    "Specular": 0.5,
    "Specular Tint": 0.0,
    "Roughness": 0.5,
    "Anisotropic": 0.0,
    "Anisotropic Rotation": 0.0,
    "Sheen": 0.0,
    "Sheen Tint": 0.5,
    "Clearcoat": 0.0,
    "Clearcoat Roughness": 0.03,
    "IOR": 1.45,
    "Transmission": 0.0,
    "Transmission Roughness": 0.0,
    "Emission": (0.0, 0.0, 0.0, 1.0),
    "Emission Strength": 1.0,
    "Alpha": 1.0,
    #"Normal": (0.0, 0.0, 1.0),
    #"Clearcoat Normal": (0.0, 0.0, 1.0),
    #"Tangent": (0.0, 0.0, 1.0),
}

MAT_DEFAULT = {
    "Specular": 0.5,
    "Roughness": 0.2,
}

MAT_SAMPLES = (
    {
        "name": "Subsurface",
        "Base Color": (1.000, 0.258, 0.123, 1.000),
        "Subsurface Color": (1.000, 0.258, 0.123, 1.000),
        "min":  0.0,
        "max":  1.0,
    }, {
        "name": "Metallic",
        "Base Color": (1.000, 0.780, 0.040, 1.000),
        "min":  0.0,
        "max":  1.0,
    }, {
        "name": "Specular",
        "Base Color": (1.000, 0.028, 0.026, 1.000),
        "min":  0.0,
        "max":  1.0,
    }, {
        "name": "Specular Tint",
        "Base Color": (1.000, 0.028, 0.026, 1.000),
        "min":  0.0,
        "max":  1.0,
    }, {
        "name": "Roughness",
        "Base Color": (0.093, 0.161, 1.000, 1.000),
        "min":  0.0,
        "max":  1.0,
    }, {
        "name": "Sheen",
        "Base Color": (0.141, 0.00083, 0.006, 1.000),
        "Roughness": 0.9,
        "Sheen Tint": 0.0,
        "min":  0.0,
        "max":  1.0,
    }, {
        "name": "Sheen Tint",
        "Base Color": (0.141, 0.00083, 0.006, 1.000),
        "Roughness": 0.9,
        "Sheen": 1.0,
        "min":  0.0,
        "max":  1.0,
    }, {
        "name": "Clearcoat",
        "Base Color": (0.011, 0.063, 0.066, 1.000),
        "Specular": 0.0,
        "min":  0.0,
        "max":  1.0,
    }, {
        "name": "Clearcoat Roughness",
        "Base Color": (0.011, 0.063, 0.066, 1.000),
        "Specular": 0.0,
        "Clearcoat": 1.0,
        "min":  0.0,
        "max":  1.0,
    }, {
        "name": "IOR",
        "Base Color": (0.238, 1.000, 0.117, 1.000),
        "Transmission": 1.0,
        "min":  1.0,
        "max":  2.0,
    }, {
        "name": "Transmission",
        "Base Color": (0.238, 1.000, 0.117, 1.000),
        "min":  0.0,
        "max":  1.0,
    }, {
        "name": "Transmission Roughness",
        "Base Color": (0.238, 1.000, 0.117, 1.000),
        "Transmission": 1.0,
        "min":  0.0,
        "max":  1.0,
    }
)


def create_bsdf_samples(nx, ny):
    w = 512
    bpy.context.scene.render.resolution_x = w
    bpy.context.scene.render.resolution_y = w * ny / nx
    bpy.context.scene.render.resolution_percentage = 100

    l = 1.1 * ny / 2 / math.tan(math.radians(39.6/2))

    cam_loc = ((nx-1)/2, -l, -(ny-1)/2)
    cam_rot = (90, 0, 0)
    cam = create_camera('Camera_0', cam_loc, cam_rot)
    add_object_to_scene(cam)

    lit_loc = (0, -5, 0)
    lit = create_light('Light_0', lit_loc, 1000)
    add_object_to_scene(lit)

    shapes_coll = create_collection("Shapes")
    add_collection_to_scene(shapes_coll)

    for j in range(0, ny):
        for i in range(0, nx):
            loc = (i, 0, -j)
            name = f"Sphere_{j}_{i}"
            obj = create_sphere(name, 0.4, loc)
            mat = create_material(name)

            # set fixed material params
            for sample in (MAT_BLENDER_DEFAULT, MAT_DEFAULT, MAT_SAMPLES[j]):
                for key in MAT_PARAM_30.keys():
                    if key in sample:
                        set_mat_param(mat, key, sample[key])

            # set a variable material param
            alpha = i/(nx-1)
            val = (1-alpha) * sample["min"] + alpha * sample["max"]
            set_mat_param(mat, sample["name"], val)

            set_obj_material(obj, mat)
            link_object_to_collection(obj, shapes_coll)

    set_mat_custom_props()


#======================================================
# UI
#======================================================
bl_info = {
    "name": "BSDF Samples",
    "author": "Takehiro Tawara",
    "version": (0, 1),
    "blender": (3, 0, 0),
    "location": "",
    "description": "create bsdf samples panel",
    "warning": "",
    "support": "TESTING",
    "doc_url": "",
    "tracker_url": "",
    "category": "Material"
}


class MY_OT_info_btn(bpy.types.Operator):
    bl_label = "Info"
    bl_idname = "my.info_btn"

    def execute(self, context):
        print(f"CWD: {os.getcwd()}")
        print(bpy.data.objects)
        print(bpy.data.materials)
        print(bpy.data.textures)
        return {'FINISHED'}


class MY_OT_clear_btn(bpy.types.Operator):
    bl_label = "Clear"
    bl_idname = "my.clear_btn"

    def execute(self, context):
        clear_all()
        return {'FINISHED'}


class MY_OT_create_btn(bpy.types.Operator):
    bl_label = "Create"
    bl_idname = "my.create_btn"

    def execute(self, context):
        create_bsdf_samples(7, len(MAT_SAMPLES))
        return {'FINISHED'}


class MY_OT_extra_btn(bpy.types.Operator):
    bl_label = "Extra"
    bl_idname = "my.extra_btn"

    def execute(self, context):
        set_mat_custom_props()
        return {'FINISHED'}


class MY_PT_ui(bpy.types.Panel):
    bl_label = "BSDF Samples"
    bl_category = "Material"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator("my.clear_btn")

        row = layout.row()
        row.operator("my.create_btn")

        row = layout.row()
        row.operator("my.extra_btn")

        row = layout.row()
        row.operator("my.info_btn")

        row = layout.row()
        row.operator("render.render")


classes = (
    MY_PT_ui,
    MY_OT_info_btn,
    MY_OT_clear_btn,
    MY_OT_create_btn,
    MY_OT_extra_btn,
)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
