import bpy 

class PHYSICS_OT_cloth_sims_collision(bpy.types.Operator): 
    """Adds a collision modifier to active object"""
    bl_idname = "physics.cloth_sims_collision"
    bl_label = "Add Collision Modifier to Active Object"

    def execute(self, context):
        """Select the object you want to add a collision modifier to"""
        obj = context.active_object
        if obj is None:
            print("No valid object selected")

        else:
            bpy.ops.object.modifier_add(type='COLLISION')

        return{"FINISHED"}