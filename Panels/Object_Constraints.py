import bpy

class VIEW3D_PT_Object_Constraints(bpy.types.Panel):
    """Object Constraints Settings Panel"""
    bl_label = "Object Constraints Settings"
    bl_idname = "VIEW3D_PT_Object_Constraints"  # Ensure to add an ID
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    bl_space_type = "VIEW_3D"  # Match parent space type
    bl_region_type = "UI"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("constraints.add_track_to_constraint", text='Add "Track To" Constraint')
        row = layout.row()
        row.operator("constraints.remove_track_to_constraint", text='Remove "Track To" Constraint')