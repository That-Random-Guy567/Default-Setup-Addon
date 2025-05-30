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
        # Get root package name (Default_Setup_Addon)
        root_package = __package__.split('.')[0]
        if root_package.startswith('bl_ext.vscode_development.'):
            root_package = root_package.replace('bl_ext.vscode_development.', '')
        
        print(f"Looking for addon with ID: {root_package}")
        
        # Try both possible paths
        for addon_id in [root_package, f"bl_ext.vscode_development.{root_package}"]:
            try:
                addon = bpy.context.preferences.addons.get(addon_id)
                if addon and addon.preferences:
                    prefs = addon.preferences
                    print(f"Found addon preferences at: {addon_id}")
                    
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
                    
                    break  # Found working preferences, stop searching
                    
            except Exception as e:
                print(f"Failed to access {addon_id}: {str(e)}")
                continue
                
    except Exception as e:
        print(f"Error in get_panels: {str(e)}")
        import traceback
        traceback.print_exc()
    
    print(f"Total panels to register: {len(panels)}")
    return panels