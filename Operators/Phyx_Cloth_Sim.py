import bpy 

class PHYSICS_OT_cloth_sims(bpy.types.Operator):
    """Adds a cloth sim to active object"""
    bl_idname = "physics.add_cloth_sim"
    bl_label = "Add Cloth Sim"
    
    def execute(self, context):
        obj = context.active_object
        if obj is None:
            print("No valid object selected")
            
        else: 
            bpy.ops.object.transform_apply(scale=True)
            bpy.ops.object.modifier_add(type='SUBSURF')
            bpy.context.object.modifiers["Subdivision"].subdivision_type = 'SIMPLE'
            bpy.context.object.modifiers["Subdivision"].levels = 4
            bpy.context.object.modifiers["Subdivision"].render_levels = 4
            bpy.ops.object.modifier_move_to_index(modifier="Subdivision", index=0)
            bpy.ops.object.modifier_set_active(modifier="Subdivision")
            bpy.ops.object.modifier_apply(modifier="Subdivision", report=True)
            
            bpy.ops.object.modifier_add(type='CLOTH')
            bpy.context.object.modifiers["Cloth"].settings.quality = 10
            bpy.context.object.modifiers["Cloth"].settings.bending_stiffness = 2
            bpy.context.object.modifiers["Cloth"].collision_settings.use_self_collision = True
            bpy.context.object.modifiers["Cloth"].collision_settings.self_distance_min = 0.001
            bpy.context.object.modifiers["Cloth"].collision_settings.distance_min = 0.005
            bpy.context.object.modifiers["Cloth"].collision_settings.collision_quality = 15

            bpy.ops.object.modifier_add(type='SUBSURF')
                  
        return{"FINISHED"}