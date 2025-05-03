import bpy 
    
class PHYSICS_OT_collision_sims_clear(bpy.types.Operator):
    """Remove Collision"""
    bl_idname = "physics.clear_collision"
    bl_label = "Clear Collisions"

    def execute(self, context):
        for obj in context.scene.objects:
            if obj.rigid_body:
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.modifier_remove(modifier="Collision")
                
        return {'FINISHED'}