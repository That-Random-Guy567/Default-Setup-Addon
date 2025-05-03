import bpy

class EXTERNAL_DATA_OT_pack_resources(bpy.types.Operator):
    """Packs external files and textures into blend file"""
    bl_idname = "external.data_pack_resources"
    bl_label = "Pack Resources"

    def execute(self, context):
        bpy.ops.file.pack_all()

        self.report({'INFO'}, "Files Packed.")
        return {"FINISHED"}