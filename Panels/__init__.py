import bpy
from .all_panels import get_panels

# Global panel lists
all_panels_old = []
_registered_panels = []  # Track currently registered panels

def refresh_panel_list():
    """Refresh the panel list when preferences change"""
    print("\n=== Refreshing Panels ===")
    try:
        print("Unregistering existing panels...")
        unregister_panels()
        
        global all_panels_old
        all_panels_old = get_panels()
        
        print("Registering updated panels...")
        register_panels()
        print("=== Refresh Complete ===\n")
    except Exception as e:
        print(f"Error during refresh: {str(e)}\n")

def register_panels():
    """Register all panels"""
    global all_panels_old, _registered_panels
    all_panels_old = get_panels()
    
    for panel in all_panels_old:
        try:
            if panel not in _registered_panels:  # Avoid duplicate registration
                bpy.utils.register_class(panel)
                _registered_panels.append(panel)
                print(f"Registered: {panel.__name__}")
        except Exception as e:
            print(f"Failed to register {panel.__name__}: {str(e)}")

def unregister_panels():
    """Unregister all panels"""
    global _registered_panels
    for panel in reversed(_registered_panels):
        try:
            bpy.utils.unregister_class(panel)
            print(f"Unregistered: {panel.__name__}")
        except Exception as e:
            print(f"Failed to unregister {panel.__name__}: {str(e)}")
    _registered_panels.clear()  # Clear tracking list after unregistering