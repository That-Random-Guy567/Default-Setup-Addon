import bpy
from bpy.props import BoolProperty, FloatProperty, IntProperty, StringProperty, EnumProperty

            
def update_panels(self, context):
    from .Panels.all_panels import refresh_panel_list
    refresh_panel_list()
    
class Default_Setup_Addon_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

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

            