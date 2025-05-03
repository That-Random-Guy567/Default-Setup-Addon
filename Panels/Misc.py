import bpy

class VIEW3D_PT_Misc(bpy.types.Panel):
    """Miscellaneous Buttons"""
    bl_label = "Miscellaneous Functions"
    bl_idname = "VIEW3D_PT_Misc"  # Ensure to add an ID
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    bl_space_type = "VIEW_3D"  # Match parent space type
    bl_region_type = "UI"
    #bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
                
        # Row for toggling specific overlays
        row = layout.row()
        row.operator("view3d.toggle_overlays", text="Toggle Specific Overlays", icon="OVERLAY")
        layout.separator()
        
        #Row for adding Rainbow Colour Ramp w bsdf
        row = layout.row()
        row.operator("material.rainbow_colour_with_principled_bsdf", text = "Add Rainbow Color Ramp with BSDF", icon = "MATERIAL")
        
        # Row for adding Rainbow Colour alone
        row = layout.row()
        row.operator("material.rainbow", text = "Add Rainbow Color Ramp", icon = "MATERIAL")

        layout.separator()
        row = layout.row()
        row.operator("world.add_nishita_sky_texture", text="Add Fine Tuned Sky Texture", icon="WORLD")