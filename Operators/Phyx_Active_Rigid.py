import bpy 


class PHYSICS_OT_active_rigid_body(bpy.types.Operator):
    """Adds an Active Rigid Body"""
    bl_idname = "physics.active_rigid_body"
    bl_label = "Add Active Rigid Body"
    
    def execute(self, context):
        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.type = 'ACTIVE'
        bpy.context.object.rigid_body.collision_shape = 'MESH'
        
        return {"FINISHED"}