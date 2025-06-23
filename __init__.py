import bpy

from .preference import Default_Setup_Addon_Preferences
from .Operators.all_operators import all_operators
from .Panels import register_panels, unregister_panels

bl_info = {
    "name": "Default Setup Addon",
    "author": "That Random Blender Guy",
    "version": (2, 0, 0),
    "blender": (4, 0, 0),
    "description": "An addon to help setup your scene with customizable preferences and default settings",
    "location": "3D Viewport > Sidebar > Default Setup",
    "category": "Development",
    # "id": "Default_Setup_Addon",
    "id": __package__,  # Use the package name for the ID
    "support": "TESTING",
    "wiki_url": "https://github.com/That-Random-Guy567/Default-Setup-Addon",
    "tracker_url": "https://github.com/That-Random-Guy567/Default-Setup-Addon/issues",
    "doc_url": "https://github.com/That-Random-Guy567/Default-Setup-Addon/blob/main/readme.md",
    "warning": "This addon is currently in Development. Not all features have been implemented yet.",
    "tags": {"User Interface", "3D View"}
}

class VIEW3D_PT_Default_Setup_Addon(bpy.types.Panel):
    bl_label = "Default Setup"
    bl_idname = "VIEW3D_PT_Default_Setup_Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Default Setup"

    def draw(self, context):
        layout = self.layout

def get_classes():
    """Get all classes that need to be registered/unregistered"""
    classes = [
        Default_Setup_Addon_Preferences,
        VIEW3D_PT_Default_Setup_Addon,
    ]
    return classes + all_operators

def register():
    print("\nRegistering Default Setup Addon...")
    try:
        for cls in get_classes():
            print(f"- Registering {cls.__name__}")
            bpy.utils.register_class(cls)
        register_panels()
        print("✓ Registration complete!\n")
    except Exception as e:
        print(f"× Registration failed: {str(e)}\n")
        raise

def unregister():
    print("\nUnregistering Default Setup Addon...")
    try:
        unregister_panels()
        for cls in reversed(get_classes()):
            print(f"- Unregistering {cls.__name__}")
            bpy.utils.unregister_class(cls)
        print("✓ Unregistration complete!\n")
    except Exception as e:
        print(f"× Unregistration failed: {str(e)}\n")
        raise

if __name__ == "__main__":
    register()