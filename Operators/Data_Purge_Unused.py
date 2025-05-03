import bpy 

class DATA_OT_purge_unused(bpy.types.Operator):
    """Purge Unused Data. WARNING DELETES ALL UNUSED DATA BLOCKS (unless saved as fake user)"""
    bl_idname = "data.purge_unused"
    bl_label = "Purge Unused Data"

    def execute(self, context):
        bpy.ops.outliner.orphans_purge()
        
        self.report({'INFO'}, "Unused data purged.")
        return {'FINISHED'}