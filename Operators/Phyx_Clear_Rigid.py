import bpy 

class PHYSICS_OT_clear_rigid_body(bpy.types.Operator):
    """Clear Rigid Bodies"""
    bl_idname = "physics.clear_rigid_body"
    bl_label = "Clear Rigid Body"
    
    def execute(self, context):
        for obj in context.scene.objects:
            if obj.rigid_body:
                bpy.context.view_layer.objects.active = obj
                bpy.ops.rigidbody.object_remove()
        return {'FINISHED'}