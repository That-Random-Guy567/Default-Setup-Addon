import bpy
from .all_operators import all_operators

def register():
    for cls in all_operators:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(all_operators):
        bpy.utils.unregister_class(cls)