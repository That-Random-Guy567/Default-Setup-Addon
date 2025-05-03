import bpy

class VIEW3D_PT_Output_Settings(bpy.types.Panel):
    """Output Settings"""
    bl_label = "Output Settings"
    bl_idname = "VIEW3D_PT_Output_Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    #bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("render.resolution_1440p", text="1440p Camera Resolution", icon="VIEW_CAMERA")
        row = layout.row()
        row.operator("render.resolution_1920x1080p", text="Portrait Camera Resolution", icon="VIEW_CAMERA")
        row = layout.row()
        row.operator("output.equal_to_exr", text="Output as EXR", icon="IMAGE_DATA")
        row = layout.row()
        row.operator("output.equal_to_mp4", text="Output as MP4", icon="FILE_MOVIE")