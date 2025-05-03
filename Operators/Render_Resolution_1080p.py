import bpy 

class RENDER_OT_change_resolution_1920x1080p(bpy.types.Operator):
    """Change Default Resolution to 1920x1080p"""
    bl_idname = "render.resolution_1920x1080p"
    bl_label = "Change the Resolution to 1920x1080p"
    
    def execute(self, context):
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080

        self.report({'INFO'}, "Camera is at 1080p in 9:16 Ratio.")
        return {'FINISHED'}