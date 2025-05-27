import bpy
from bpy.props import BoolProperty, FloatProperty, IntProperty, StringProperty, EnumProperty

            
def update_panels(self, context):
    print("\n=== Preferences Update Called ===")
    print(f"Physics enabled: {self.enable_physics}")
    print(f"Rigid Body enabled: {self.enable_rigid_body}")
    print(f"Cloth enabled: {self.enable_cloth}")
    
    from .Panels.all_panels import refresh_panel_list
    refresh_panel_list()
    
    print("Forcing UI redraw...")
    for area in context.screen.areas:
        if area.type == 'VIEW_3D':
            area.tag_redraw()
    print("=== Update Complete ===\n")
    
class Default_Setup_Addon_Preferences(bpy.types.AddonPreferences):
    bl_idname = "default_setup_addon"

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

            