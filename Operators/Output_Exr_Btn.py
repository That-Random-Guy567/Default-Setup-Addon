import bpy

class OUTPUT_OT_exr_video_button(bpy.types.Operator):
    """Changes file output to exr"""
    bl_idname = "output.equal_to_exr"
    bl_label = "Change Output to EXR"
    
    def execute(self, context):
        scene = context.scene  # Access context instead of bpy.context
        
        # Set the render settings for EXR
        scene.render.image_settings.file_format = 'OPEN_EXR'
        scene.render.image_settings.color_mode = 'RGBA'
        scene.render.image_settings.exr_codec = 'DWAA'
        scene.render.image_settings.quality = 90

        self.report({'INFO'}, "Output set as OpenEXR File.")
        return {"FINISHED"}