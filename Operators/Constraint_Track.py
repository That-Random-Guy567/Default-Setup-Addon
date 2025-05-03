import bpy 


class CONSTRAINT_OT_add_track_to_constraint(bpy.types.Operator):
    """Adding the object constraint of 'Track To' to an object"""
    bl_idname = "constraints.add_track_to_constraint"
    bl_label = 'Add "Track To" to an object'
    
    def execute(self, context):
        bpy.ops.object.constraint_add(type='TRACK_TO')

        return {"FINISHED"}