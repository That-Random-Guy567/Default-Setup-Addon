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
        row.operator("render.resolution_1080x1920p", text="1080x1920p Resolution", icon="VIEW_CAMERA")
        row = layout.row()
        row.operator("output.local_dir", text="Local Output", icon="FILE_FOLDER")
        row = layout.row()
        row.operator("output.equal_to_exr", text="EXR Output", icon="IMAGE_DATA")
        row.operator("output.equal_to_mp4", text="MP4 Output", icon="FILE_MOVIE")
        