import bpy 

class PHYSICS_OT_cloth_sims_clear(bpy.types.Operator):
    """Remove Cloth Sim"""
    bl_idname = "physics.clear_cloth_sims"
    bl_label = "Clear Cloth Sims"
    
    def execute(self, context):
        for obj in context.scene.objects:
            if obj.rigid_body:
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.modifier_remove(modifier="Cloth")
                
        return {'FINISHED'}