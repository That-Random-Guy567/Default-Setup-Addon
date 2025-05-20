import bpy

from .File_Sharing import VIEW3D_PT_File_Sharing
from .Misc import VIEW3D_PT_Misc
from .Object_Constraints import VIEW3D_PT_Object_Constraints
from .Output_Settings import VIEW3D_PT_Output_Settings
from .Physics_Tab import VIEW3D_PT_Physics_Tab_Settings
from .Physics_Tab import VIEW3D_PT_Rigid_Bodies
from .Physics_Tab import VIEW3D_PT_Cloth_sims
from .Render_Settings import VIEW3D_PT_Render_Settings

all_panels = []  # ← just initialize as empty

def get_panels():
    """Get list of panels based on preferences"""
    panels = [
        VIEW3D_PT_Render_Settings,
        VIEW3D_PT_Output_Settings,
        VIEW3D_PT_File_Sharing,
        VIEW3D_PT_Object_Constraints,
        VIEW3D_PT_Misc,
    ]
    
    try:
    #   prefs = bpy.context.preferences.addons[__package__].preferences
        prefs = bpy.context.preferences.addons["Default_Setup_Addon"].preferences
        
        if prefs.enable_physics:
            panels.append(VIEW3D_PT_Physics_Tab_Settings)
            if prefs.enable_rigid_body:
                panels.append(VIEW3D_PT_Rigid_Bodies)
            if prefs.enable_cloth:
                panels.append(VIEW3D_PT_Cloth_sims)
                
    except (KeyError, AttributeError):
        pass
    
    return panels

def refresh_panel_list():
    """Refresh the panel list when preferences change"""
    try:
        unregister_panels()
        global all_panels
        all_panels = get_panels()
        register_panels()
    except Exception as e:
        print(f"Error refreshing panel list: {e}")

def register_panels():
    global all_panels
    all_panels = get_panels()

    for panel in all_panels:
        try:
            bpy.utils.register_class(panel)
        except ValueError:
            pass

def unregister_panels():
    for panel in reversed(all_panels):
        try:
            bpy.utils.unregister_class(panel)
        except RuntimeError:
            pass