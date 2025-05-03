import bpy

class VIEW3D_OT_toggle_overlays(bpy.types.Operator):
    """Toggle Overlays"""
    bl_idname = "view3d.toggle_overlays"
    bl_label = "Toggle Overlays"
    
    def execute(self, context):
        overlay = context.space_data.overlay
        context.space_data.overlay.show_stats = True
        overlay.show_axis_z = not overlay.show_axis_z  # Toggle the Z-axis overlay
        return {"FINISHED"}