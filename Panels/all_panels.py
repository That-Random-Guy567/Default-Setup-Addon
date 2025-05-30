import bpy

from .File_Sharing import VIEW3D_PT_File_Sharing
from .Misc import VIEW3D_PT_Misc
from .Object_Constraints import VIEW3D_PT_Object_Constraints
from .Output_Settings import VIEW3D_PT_Output_Settings
from .Physics_Tab import VIEW3D_PT_Physics_Tab_Settings
from .Physics_Tab import VIEW3D_PT_Rigid_Bodies
from .Physics_Tab import VIEW3D_PT_Cloth_sims
from .Render_Settings import VIEW3D_PT_Render_Settings

def get_panels():
    """Get list of panels based on preferences"""
    print("\n=== Getting Panels ===")
    panels = [
        VIEW3D_PT_Render_Settings,
        VIEW3D_PT_Output_Settings,
        VIEW3D_PT_File_Sharing,
        VIEW3D_PT_Object_Constraints,
        VIEW3D_PT_Misc,
    ]
    
    try:
        # Try both possible package paths
        try:
            prefs = bpy.context.preferences.addons[__package__.split('.')[0]].preferences
        except KeyError:
            # Fallback for development path
            prefs = bpy.context.preferences.addons["bl_ext.vscode_development." + __package__.split('.')[0]].preferences

        print(f"Preferences loaded successfully:")
        print(f"- Physics: {prefs.enable_physics}")
        print(f"- Rigid Body: {prefs.enable_rigid_body}")
        print(f"- Cloth: {prefs.enable_cloth}")
        
        if prefs.enable_physics:
            print("Adding Physics panel")
            panels.append(VIEW3D_PT_Physics_Tab_Settings)
            if prefs.enable_rigid_body:
                print("Adding Rigid Body panel")
                panels.append(VIEW3D_PT_Rigid_Bodies)
            if prefs.enable_cloth:
                print("Adding Cloth panel")
                panels.append(VIEW3D_PT_Cloth_sims)
                
    except KeyError:
        print(f"Error: Addon ID not found in preferences. Package: {__package__}")
    except AttributeError as e:
        print(f"Error accessing preferences: {str(e)}")
    
    print(f"Total panels to register: {len(panels)}")
    return panels