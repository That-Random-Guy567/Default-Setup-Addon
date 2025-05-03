import bpy 

class CONSTRAINT_OT_remove_track_to_constraint(bpy.types.Operator):
    """Removing the object constraint of 'Track To' from an object"""
    bl_idname = "constraints.remove_track_to_constraint"
    bl_label = 'Remove "Track To" from an object'
    
    def execute(self, context):
        if context.object and context.object.constraints.get("Track"):
            bpy.ops.constraint.delete(constraint="Track", owner='OBJECT')
        return {"FINISHED"}