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
    print("\n=== Getting Panels ===")
    panels = [
        VIEW3D_PT_Render_Settings,
        VIEW3D_PT_Output_Settings,
        VIEW3D_PT_File_Sharing,
        VIEW3D_PT_Object_Constraints,
        VIEW3D_PT_Misc,
    ]
    
    try:
        prefs = bpy.context.preferences.addons["default_setup_addon"].preferences
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
                
    except (KeyError, AttributeError) as e:
        print(f"Error accessing preferences: {str(e)}")
    
    print(f"Total panels to register: {len(panels)}")
    print("=== Panel Collection Complete ===\n")
    return panels

def refresh_panel_list():
    """Refresh the panel list when preferences change"""
    print("\n=== Refreshing Panels ===")
    try:
        print("Unregistering existing panels...")
        unregister_panels()
        global all_panels
        all_panels = get_panels()
        print("Registering new panels...")
        register_panels()
        print("=== Refresh Complete ===\n")
    except Exception as e:
        print(f"Error during refresh: {str(e)}\n")

def register_panels():
    print("\n=== Registering Panels ===")
    global all_panels
    all_panels = get_panels()

    for panel in all_panels:
        try:
            print(f"Registering: {panel.__name__}")
            bpy.utils.register_class(panel)
        except ValueError as e:
            print(f"Failed to register {panel.__name__}: {str(e)}")
    print("=== Registration Complete ===\n")

def unregister_panels():
    print("\n=== Unregistering Panels ===")
    for panel in reversed(all_panels):
        try:
            print(f"Unregistering: {panel.__name__}")
            bpy.utils.unregister_class(panel)
        except RuntimeError as e:
            print(f"Failed to unregister {panel.__name__}: {str(e)}")
    print("=== Unregistration Complete ===\n")