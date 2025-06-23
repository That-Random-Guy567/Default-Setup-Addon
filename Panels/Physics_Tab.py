import bpy

class VIEW3D_PT_Physics_Tab_Settings(bpy.types.Panel):
    """Rigid Body Settings Panel"""
    bl_label = "Physics Settings"
    bl_idname = "VIEW3D_PT_Physics_Tab_Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Default Setup"

    @classmethod
    def poll(cls, context):
        prefs = bpy.context.preferences.addons[__package__].preferences
        return getattr(prefs, "enable_physics", False)

    def draw(self, context):
        layout = self.layout
        layout.label(text="Physics Tools")

        prefs = context.preferences.addons[__package__].preferences

        # Only show rigid body operators if enabled
        if prefs.enable_rigid_body:
            box = layout.box()
            box.label(text="Rigid Body Tools")
            box.operator("physics.active_rigid_body")
            box.operator("physics.passive_rigid_body")
            box.operator("physics.clear_rigid_body")

        # Only show cloth operators if enabled
        if prefs.enable_cloth:
            box = layout.box()
            box.label(text="Cloth Tools")
            box.operator("physics.cloth_sims")
            box.operator("physics.cloth_sims_clear")

class VIEW3D_PT_Rigid_Bodies(bpy.types.Panel):
    """Rigid Bodies"""
    bl_label = "Rigid Bodies"
    bl_idname = "VIEW3D_PT_Rigid_Bodies"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Physics_Tab_Settings"
    #bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        row = layout.row()

        row.label(text="Rigid Bodies")
        row = layout.row(align=True)  # Corrected to align buttons
        row.operator("physics.active_rigid_body", text="Active Collision", icon="RIGID_BODY")
        row.operator("physics.passive_rigid_body", text="Passive Collision", icon="RIGID_BODY")
        row = layout.row()
        row.operator("physics.clear_rigid_body", text="Clear Active Rigid Bodies", icon="CANCEL")
        layout.separator()

    @classmethod
    def poll(cls, context):
        prefs = bpy.context.preferences.addons[__package__].preferences
        return prefs.enable_physics and prefs.enable_rigid_body
        
class VIEW3D_PT_Cloth_sims(bpy.types.Panel):
    """Cloth Simulations"""
    bl_label = "Cloth Simulations"
    bl_idname = "VIEW3D_PT_Cloth_sims"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Physics_Tab_Settings"
    #bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        row = layout.row()

        row.label(text ="Cloth Simulations")
        row = layout.row()
        row.operator("physics.add_cloth_sim", text = "Add Cloth Sim", icon="MOD_CLOTH")
        row = layout.row()
        row.operator("physics.cloth_sims_collision", text = "Add Collision to Active Object", icon="MOD_PHYSICS")
        row = layout.row()
        row.operator("physics.clear_cloth_sims", text = "Clear Cloth Sim", icon = "CANCEL")
        row.operator("physics.clear_collision", text = "Clear Collisons", icon = "CANCEL")

    @classmethod
    def poll(cls, context):
        prefs = context.preferences.addons[__package__].preferences
        return prefs.enable_physics and prefs.enable_cloth