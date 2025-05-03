import bpy 

class RENDER_OT_change_resolution_1440p(bpy.types.Operator):
    """Change Default Resolution to 1440p"""
    bl_idname = "render.resolution_1440p"
    bl_label = "Change the Resolution to 1440p"
    
    def execute(self, context):
        bpy.context.scene.render.resolution_x = 2560
        bpy.context.scene.render.resolution_y = 1440 

        self.report({'INFO'}, "Camera is at 1440p Resolution.")
        return {'FINISHED'}   