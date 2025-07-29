import bpy

class VIEW3D_PT_Physics_Tab(bpy.types.Panel):
    """Physics Tab (Parent for Physics Tools)"""
    bl_label = "Physics Tab"
    bl_idname = "VIEW3D_PT_Physics_Tab"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Default Setup"
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"

    @classmethod
    def poll(cls, context):
        prefs = context.preferences.addons["bl_ext.user_default.Default_Setup_Addon"].preferences
        return prefs.enable_physics

    def draw(self, context):
        layout = self.layout
        #layout.label(text="Configure Physics Tools in Preferences.")

class VIEW3D_PT_Rigid_Bodies(bpy.types.Panel):
    """Rigid Bodies"""
    bl_label = "Rigid Bodies"
    bl_idname = "VIEW3D_PT_Rigid_Bodies"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Default Setup"
    bl_parent_id = "VIEW3D_PT_Physics_Tab"

    @classmethod
    def poll(cls, context):
        prefs = context.preferences.addons["bl_ext.user_default.Default_Setup_Addon"].preferences
        return prefs.enable_physics and prefs.enable_rigid_body

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Rigid Bodies")
        row = layout.row(align=True)
        row.operator("physics.active_rigid_body", text="Active Collision", icon="RIGID_BODY")
        row.operator("physics.passive_rigid_body", text="Passive Collision", icon="RIGID_BODY")
        row = layout.row()
        row.operator("physics.clear_rigid_body", text="Clear Active Rigid Bodies", icon="CANCEL")
        layout.separator()

class VIEW3D_PT_Cloth_sims(bpy.types.Panel):
    """Cloth Simulations"""
    bl_label = "Cloth Simulations"
    bl_idname = "VIEW3D_PT_Cloth_sims"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Default Setup"
    bl_parent_id = "VIEW3D_PT_Physics_Tab"

    @classmethod
    def poll(cls, context):
        prefs = context.preferences.addons["bl_ext.user_default.Default_Setup_Addon"].preferences
        return prefs.enable_physics and prefs.enable_cloth

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Cloth Simulations")
        row = layout.row()
        row.operator("physics.add_cloth_sim", text="Add Cloth Sim", icon="MOD_CLOTH")
        row = layout.row()
        row.operator("physics.cloth_sims_collision", text="Add Collision to Active Object", icon="MOD_PHYSICS")
        row = layout.row()
        row.operator("physics.clear_cloth_sims", text="Clear Cloth Sim", icon="CANCEL")
        row.operator("physics.clear_collision", text="Clear Collisons", icon="CANCEL")