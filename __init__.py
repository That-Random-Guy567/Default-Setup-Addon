import bpy

bl_info = {
    "name": "Default Setup Addon",
    "author": "That Random Blender Guy",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "3D Viewport > Sidebar > Default Setup Addon",
    "description": "Changes Default Settings to a template",
    "category": "Development",
}

from .Operators.all_operators import all_operators
from .Panels.all_panels import all_panels

class VIEW3D_PT_Default_Setup_Addon(bpy.types.Panel):
    bl_label = "Default Setup"
    bl_idname = "VIEW3D_PT_Default_Setup_Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Default Setup"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

classes = [
    VIEW3D_PT_Default_Setup_Addon,
]

def register():
    for register_list in (classes, all_operators, all_panels):
        for cls in register_list:
            if hasattr(cls, "bl_rna"):  # avoid double-register
                bpy.utils.register_class(cls)

def unregister():
    for register_list in (reversed(classes), reversed(all_operators), reversed(all_panels)):
        for cls in register_list:
            if hasattr(cls, "bl_rna"):
                bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
