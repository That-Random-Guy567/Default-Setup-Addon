import bpy
from bpy.props import BoolProperty, FloatProperty, IntProperty, StringProperty, EnumProperty


def update_panels(self, context):
    """Callback when preferences are changed"""
    print("\n=== Preferences Update Called ===")
    print(f"Physics enabled: {self.enable_physics}")
    print(f"Rigid Body enabled: {self.enable_rigid_body}")
    print(f"Cloth enabled: {self.enable_cloth}")
    # Force UI update
    for window in context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()

class Default_Setup_Addon_Preferences(bpy.types.AddonPreferences):
    #bl_idname = "Default_Setup_Addon"
    bl_idname = __package__
    #bl_idname = __package__.split('.')[0]
    

    enable_physics: bpy.props.BoolProperty( #type: ignore
        name="Enable Physics Tab",
        default=False,
        update=update_panels
    )

    enable_rigid_body: bpy.props.BoolProperty( #type: ignore
        name="Enable Rigid Body Tools",
        default=False,
        update=update_panels
    )

    enable_cloth: bpy.props.BoolProperty( #type: ignore
        name="Enable Cloth Tools",
        default=False,
        update=update_panels
    )

    def draw(self, context):
        layout = self.layout
        
        box_physics = layout.box()
        box_physics.prop(self, "enable_physics")
        
        # Only show sub-options if physics is enabled
        if self.enable_physics:
            sub = box_physics.box()
            sub.prop(self, "enable_cloth")
            sub.prop(self, "enable_rigid_body")
            
"""
def register():
    bpy.utils.register_class(Default_Setup_Addon_Preferences)
    
def unregister():
    bpy.utils.unregister_class(Default_Setup_Addon_Preferences)
"""