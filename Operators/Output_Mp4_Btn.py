import bpy 

class OUTPUT_OT_mp4_video_button(bpy.types.Operator):
    """Changes file output to mp4"""
    bl_idname = "output.equal_to_mp4"
    bl_label = "Change Output to MP4"
    
    def execute(self, context):
        scene = context.scene  # Access context instead of bpy.context
        
        # Set the render settings for MP4
        scene.render.image_settings.file_format = 'FFMPEG'
        scene.render.ffmpeg.format = 'MPEG4'
        scene.render.ffmpeg.constant_rate_factor = 'HIGH'
        scene.render.ffmpeg.audio_codec = 'NONE'
        
        self.report({'INFO'}, "Output settings changed to MP4.")
        return {"FINISHED"}