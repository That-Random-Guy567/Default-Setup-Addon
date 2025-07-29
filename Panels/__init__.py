import bpy
from .File_Sharing import VIEW3D_PT_File_Sharing
from .Misc import VIEW3D_PT_Misc
from .Object_Constraints import VIEW3D_PT_Object_Constraints
from .Output_Settings import VIEW3D_PT_Output_Settings
from .Physics_Tab import VIEW3D_PT_Rigid_Bodies, VIEW3D_PT_Cloth_sims, VIEW3D_PT_Physics_Tab
from .Render_Settings import VIEW3D_PT_Render_Settings

panel_classes = [
    VIEW3D_PT_Render_Settings,
    VIEW3D_PT_Output_Settings,
    VIEW3D_PT_File_Sharing,
    VIEW3D_PT_Physics_Tab,
    VIEW3D_PT_Object_Constraints,
    VIEW3D_PT_Misc,
    VIEW3D_PT_Rigid_Bodies,
    VIEW3D_PT_Cloth_sims,
]

def register_panels():
    for cls in panel_classes:
        bpy.utils.register_class(cls)

def unregister_panels():
    for cls in reversed(panel_classes):
        bpy.utils.unregister_class(cls)