import bpy

class VIEW3D_PT_File_Sharing(bpy.types.Panel):
    """File Sharing"""
    bl_label = "File Sharing"
    bl_idname = "VIEW3D_PT_File_Sharing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("external.data_pack_resources", text="Pack Resources", icon="PACKAGE")
        row = layout.row()
        row.operator("external.data_relative_files", text="Make Paths Relative", icon="FILEBROWSER")
        row = layout.row()
        row.operator("data.purge_unused", text = "Delete Unused Data", icon = "TRASH")