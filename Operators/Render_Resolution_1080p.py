import bpy 

class RENDER_OT_change_resolution_1080x1920p(bpy.types.Operator):
    """Change Default Resolution to 1080x1920p"""
    bl_idname = "render.resolution_1080x1920p"
    bl_label = "Change the Resolution to 1080x1920p"
    
    def execute(self, context):
        bpy.context.scene.render.resolution_x = 1080
        bpy.context.scene.render.resolution_y = 1920

        self.report({'INFO'}, "Camera is in 9:16 Ratio.")
        return {'FINISHED'}