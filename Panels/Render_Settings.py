import bpy

class VIEW3D_PT_Render_Settings(bpy.types.Panel):
    """Render Settings"""
    bl_label = "Render Settings"
    bl_idname = "VIEW3D_PT_Render_Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    #bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("render.cycle_gpu_button", text="Render Engine to Cycles", icon="OUTLINER_OB_CAMERA")
        row = layout.row()
        row.operator("render.render_optimization", text="Optimize Render", icon="SHADING_RENDERED")
