import bpy

from .File_Sharing import VIEW3D_PT_File_Sharing
from .Misc import VIEW3D_PT_Misc
from .Object_Constraints import VIEW3D_PT_Object_Constraints
from .Output_Settings import VIEW3D_PT_Output_Settings
from .Physics_Tab import VIEW3D_PT_Physics_Tab_Settings
from .Physics_Tab import VIEW3D_PT_Rigid_Bodies
from .Physics_Tab import VIEW3D_PT_Cloth_sims
from .Render_Settings import VIEW3D_PT_Render_Settings


all_panels = [
# change order = change ui
    VIEW3D_PT_Render_Settings,
    VIEW3D_PT_Output_Settings,
    VIEW3D_PT_File_Sharing,
    VIEW3D_PT_Physics_Tab_Settings,
    VIEW3D_PT_Rigid_Bodies,
    VIEW3D_PT_Cloth_sims,
    VIEW3D_PT_Object_Constraints,
    VIEW3D_PT_Misc,
]