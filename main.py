bl_info = {
    "name": "Default Setup Addon",
    "author": "That Random Blender Guy",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "3D Viewport > Sidebar > Default Setup Addon",
    "description": "Changes Default Settings to a template",
    "category": "Development",
}

import bpy


#------------------------------------------------------Parent Panel UI Settings--------------------------------------------------------  
class VIEW3D_PT_Default_Setup_Addon(bpy.types.Panel):
    bl_label = "Default Setup"
    bl_idname = "VIEW3D_PT_Default_Setup_Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Default Setup"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
#------------------------------------------------------Child Panel: Render Settings---------------------------------------------------

class VIEW3D_PT_Render_Settings(bpy.types.Panel):
    """Render Settings"""
    bl_label = "Render Settings"
    bl_idname = "VIEW3D_PT_Render_Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    #bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("render.cycle_gpu_button", text="Render Engine to Cycles", icon="OUTLINER_OB_CAMERA")
        row = layout.row()
        row.operator("render.render_optimization", text="Optimize Render", icon="SHADING_RENDERED")
        
        
        # Row for adding the Nishita sky texture
        row = layout.row()
        row.operator("world.add_nishita_sky_texture", text="Add Fine Tuned Sky Texture", icon="WORLD")

#------------------------------------------------------Child Panel: Output Settings---------------------------------------------------

class VIEW3D_PT_Output_Settings(bpy.types.Panel):
    """Output Settings"""
    bl_label = "Output Settings"
    bl_idname = "VIEW3D_PT_Output_Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    #bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("render.resolution_1440p", text="1440p Camera Resolution", icon="VIEW_CAMERA")
        row = layout.row()
        row.operator("render.resolution_1920x1080p", text="Portrait Camera Resolution", icon="VIEW_CAMERA")
        row = layout.row()
        row.operator("output.equal_to_exr", text="Output as EXR", icon="IMAGE_DATA")
        row = layout.row()
        row.operator("output.equal_to_mp4", text="Output as MP4", icon="FILE_MOVIE")

#------------------------------------------------------Child Panel: File Sharing---------------------------------------------------
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
        

#-----------------------------------------------------Child Panel: Physics Tab Settings------------------------------------------------

class VIEW3D_PT_Physics_Tab_Settings(bpy.types.Panel):
    """Rigid Body Settings Panel"""
    bl_label = "Physics Settings"
    bl_idname = "VIEW3D_PT_Physics_Tab_Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()   

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
        row.operator("physics.cloth_sims", text = "Add Cloth Sim", icon="MOD_CLOTH")
        row = layout.row()
        row.operator("physics.cloth_sims_collision", text = "Add Collision to Active Object", icon="MOD_PHYSICS")
        row = layout.row()
        row.operator("physics.clear_cloth_sims", text = "Clear Cloth Sim", icon = "CANCEL")
        row.operator("physics.clear_collision", text = "Clear Collisons")

#-------------------------------------------------------Child Panel: Object Constraints---------------------------------------------------
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
                
        

#-------------------------------------------------------Child Panel: Miscellaneous Things---------------------------------------------

class VIEW3D_PT_Misc(bpy.types.Panel):
    """Miscellaneous Buttons"""
    bl_label = "Miscellaneous Functions"
    bl_idname = "VIEW3D_PT_Misc"  # Ensure to add an ID
    bl_parent_id = "VIEW3D_PT_Default_Setup_Addon"
    bl_space_type = "VIEW_3D"  # Match parent space type
    bl_region_type = "UI"
    #bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
                
        # Row for toggling specific overlays
        row = layout.row()
        row.operator("view3d.toggle_overlays", text="Toggle Specific Overlays", icon="OVERLAY")
        layout.separator()
        
        #Row for adding Rainbow Colour Ramp w bsdf
        row = layout.row()
        row.operator("material.rainbow_colour_with_principled_bsdf", text = "Add Rainbow Color Ramp with BSDF", icon = "MATERIAL")
        
        # Row for adding Rainbow Colour alone
        row = layout.row()
        row.operator("material.rainbow", text = "Add Rainbow Color Ramp", icon = "MATERIAL")

################################################################-----{OPERATOR DEFINING HERE}-----#########################################################
        

#                                                                   Changing Render Settings

class RENDER_OT_cycle_gpu_button(bpy.types.Operator):
    """Change Render Settings to Cycles to work on the GPU"""
    bl_idname = "render.cycle_gpu_button"
    bl_label = "Change the Render Settings to Cycles on GPU"
    
    def execute(self, context):
        context.scene.render.engine = 'CYCLES'
        context.scene.cycles.device = 'GPU'
        context.scene.cycles.preview_samples = 100
        context.scene.cycles.use_preview_denoising = True
        context.scene.cycles.samples = 75
        context.scene.render.use_motion_blur = True
        context.scene.render.motion_blur_shutter = 0.5
        context.scene.render.use_persistent_data = True

        self.report({'INFO'}, "Cycles is now enabled on GPU.")
        return {"FINISHED"}
#------------------------------------------------------------ Render Optimizations ------------------------------------------------
class RENDER_OT_render_optimization(bpy.types.Operator):
    """Optimzes rendering settings"""
    bl_idname = "render.render_optimization"
    bl_label = "Optimizes rendering settings"

    def execute(self, context):
        render = bpy.context.scene.render
        cycles = bpy.context.scene.cycles

        cycles.max_bounces = 8
        #cycles.caustics_reflective = False
        #cycles.caustics_refractive = False
        cycles.diffuse_bounces = 1
        cycles.glossy_bounces = 4
        cycles.transmission_bounces = 8
        cycles.volume_bounces = 2
        cycles.transparent_max_bounces = 8
        cycles.use_fast_gi = True
        cycles.ao_bounces = 2
        cycles.ao_bounces_render = 2
        cycles.debug_use_spatial_splits = True
        cycles.debug_use_compact_bvh = False
        cycles.debug_use_hair_bvh = True
        cycles.debug_bvh_time_steps = 2
        cycles.use_auto_tile = True
        cycles.tile_size = 2048
        cycles.texture_limit_render = '2048'
        cycles.use_camera_cull = True
        cycles.device = 'GPU'
        cycles.denoiser = 'OPENIMAGEDENOISE'
        cycles.denoising_use_gpu = True


        render.threads_mode = 'AUTO'
        render.use_persistent_data = True
        render.use_simplify = True
        render.compositor_device = 'GPU'
        render.simplify_subdivision_render = 4

        self.report({'INFO'}, "Rendering Settings Optimized")
        return {'FINISHED'}
        
#------------------------------------------------------------ 1440p res------------------------------------------------

class RENDER_OT_change_resolution_1440p(bpy.types.Operator):
    """Change Default Resolution to 1440p"""
    bl_idname = "render.resolution_1440p"
    bl_label = "Change the Resolution to 1440p"
    
    def execute(self, context):
        bpy.context.scene.render.resolution_x = 2560
        bpy.context.scene.render.resolution_y = 1440 

        self.report({'INFO'}, "Camera is at 1440p Resolution.")
        return {'FINISHED'}    

#------------------------------------------------------------ 1920x1080p res ----------------------------------------------------
class RENDER_OT_change_resolution_1920x1080p(bpy.types.Operator):
    """Change Default Resolution to 1920x1080p"""
    bl_idname = "render.resolution_1920x1080p"
    bl_label = "Change the Resolution to 1920x1080p"
    
    def execute(self, context):
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080

        self.report({'INFO'}, "Camera is at 1080p in 9:16 Ratio.")
        return {'FINISHED'}
    

#------------------------------------------------------ Export as EXR ------------------------------------------------
class OUTPUT_OT_exr_video_button(bpy.types.Operator):
    """Changes file output to exr"""
    bl_idname = "output.equal_to_exr"
    bl_label = "Change Output to EXR"
    
    def execute(self, context):
        scene = context.scene  # Access context instead of bpy.context
        
        # Set the render settings for EXR
        scene.render.image_settings.file_format = 'OPEN_EXR'
        scene.render.image_settings.color_mode = 'RGBA'
        scene.render.image_settings.exr_codec = 'DWAA'
        scene.render.image_settings.quality = 90

        self.report({'INFO'}, "Output set as OpenEXR File.")
        return {"FINISHED"}

#-----------------------------------------------------------MP4 Video Output------------------------------------------
class OUTPUT_OT_mp4_video_button(bpy.types.Operator):
    """Changes file output to mp4"""
    bl_idname = "output.equal_to_mp4"
    bl_label = "Change Output to MP4"
    
    def execute(self, context):
        scene = context.scene  # Access context instead of bpy.context
        
        # Set the render settings for MP4
        scene.render.image_settings.file_format = 'FFMPEG'
        scene.render.ffmpeg.format = 'MPEG4'
        scene.render.ffmpeg.constant_rate_factor = 'HIGH'
        scene.render.ffmpeg.audio_codec = 'NONE'
        
        self.report({'INFO'}, "Output settings changed to MP4.")
        return {"FINISHED"}

#-----------------------------------------------------------Pack Resources------------------------------------------  
class EXTERNAL_DATA_OT_pack_resources(bpy.types.Operator):
    """Packs external files and textures into blend file"""
    bl_idname = "external.data_pack_resources"
    bl_label = "Pack Resources"

    def execute(self, context):
        bpy.ops.file.pack_all()

        self.report({'INFO'}, "Files Packed.")
        return {"FINISHED"}


#----------------------------------------------------------- Relative File Locations------------------------------------------
class EXTERNAL_DATA_OT_relative_files(bpy.types.Operator):
    """Makes all external files and textures have relative file path"""
    bl_idname = "external.data_relative_files"
    bl_label = "Relative Files"

    def execute(self, context):
        bpy.ops.file.make_paths_relative()

        self.report({'INFO'}, "Files Paths Made Relative.")
        return {"FINISHED"}

#----------------------------------------------------Purging Unused Data Blocks-------------------------------------------------

class DATA_OT_purge_unused(bpy.types.Operator):
    """Purge Unused Data. WARNING DELETES ALL UNUSED DATA BLOCKS (unless saved as fake user)"""
    bl_idname = "data.purge_unused"
    bl_label = "Purge Unused Data"

    def execute(self, context):
        bpy.ops.outliner.orphans_purge()
        
        self.report({'INFO'}, "Unused data purged.")
        return {'FINISHED'}

#------------------------------------------------------Adding Nishita Sky Texture------------------------------------------------   

class WORLD_OT_sky_texture_button(bpy.types.Operator):
    """Adds the Nishita Sky Texture that is already fine-tuned"""
    bl_idname = "world.add_nishita_sky_texture"
    bl_label = "Adds Fine Tuned Sky Texture"

    def execute(self, context):
        world = bpy.data.worlds.get("World") or bpy.data.worlds.new("World")
        world.use_nodes = True
        node_tree = world.node_tree

        # Clear all existing nodes
        for node in node_tree.nodes:
            node_tree.nodes.remove(node)

        # Add a World Output node
        world_output_node = node_tree.nodes.new(type="ShaderNodeOutputWorld")

        # Add a background node
        background_node = node_tree.nodes.new(type="ShaderNodeBackground")

        # Add a Nishita sky texture node
        nishita_node = node_tree.nodes.new(type="ShaderNodeTexSky")
        nishita_node.sky_type = 'NISHITA'

        # Link the nodes
        node_tree.links.new(nishita_node.outputs[0], background_node.inputs[0])
        node_tree.links.new(background_node.outputs[0], world_output_node.inputs[0])

        # Adjusting the sky texture
        nishita_node.sun_elevation = 45.0
        nishita_node.sun_rotation = 0.0
        background_node.inputs[1].default_value = 0.3

        print("Nishita sky texture applied!")
        return {'FINISHED'}

#----------------------------------------------------------Adding Object Constraints---------------------------------------------
class CONSTRAINT_OT_add_track_to_constraint(bpy.types.Operator):
    """Adding the object constraint of 'Track To' to an object"""
    bl_idname = "constraints.add_track_to_constraint"
    bl_label = 'Add "Track To" to an object'
    
    def execute(self, context):
        bpy.ops.object.constraint_add(type='TRACK_TO')
        
        return {"FINISHED"}
    
class CONSTRAINT_OT_remove_track_to_constraint(bpy.types.Operator):
    """Removing the object constraint of 'Track To' from an object"""
    bl_idname = "constraints.remove_track_to_constraint"
    bl_label = 'Remove "Track To" from an object'
    
    def execute(self, context):
        if context.object and context.object.constraints.get("Track"):
            bpy.ops.constraint.delete(constraint="Track", owner='OBJECT')
        return {"FINISHED"}
    
#-----------------------------------------------------Viewport Overlay Settings---------------------------------------------------
        
class VIEW3D_OT_toggle_overlays(bpy.types.Operator):
    """Toggle Overlays"""
    bl_idname = "view3d.toggle_overlays"
    bl_label = "Toggle Overlays"
    
    def execute(self, context):
        overlay = context.space_data.overlay
        context.space_data.overlay.show_stats = True
        overlay.show_axis_z = not overlay.show_axis_z  # Toggle the Z-axis overlay
        return {"FINISHED"}
    
#-------------------------------------------------------Adding Custom Rigid Body---------------------------------------------------


class PHYSICS_OT_passive_rigid_body(bpy.types.Operator):
    """Adds a Passive Rigid Body"""  
    bl_idname = "physics.passive_rigid_body"
    bl_label = "Add Passive Rigid Body"
    
    def execute(self, context):
        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.type = 'PASSIVE'
        bpy.context.object.rigid_body.collision_shape = 'MESH'
        
        return {"FINISHED"}
    
class PHYSICS_OT_active_rigid_body(bpy.types.Operator):
    """Adds an Active Rigid Body"""
    bl_idname = "physics.active_rigid_body"
    bl_label = "Add Active Rigid Body"
    
    def execute(self, context):
        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.type = 'ACTIVE'
        bpy.context.object.rigid_body.collision_shape = 'MESH'
        
        return {"FINISHED"}
    
class PHYSICS_OT_clear_rigid_body(bpy.types.Operator):
    """Clear Rigid Bodies"""
    bl_idname = "physics.clear_rigid_body"
    bl_label = "Clear Rigid Body"
    
    def execute(self, context):
        for obj in context.scene.objects:
            if obj.rigid_body:
                bpy.context.view_layer.objects.active = obj
                bpy.ops.rigidbody.object_remove()
        return {'FINISHED'}
    
#--------------------------------------------------------------Cloth Simulations ----------------------------------------------------

class PHYSICS_OT_cloth_sims(bpy.types.Operator):
    """Adds a cloth sim to active object"""
    bl_idname = "physics.cloth_sims"
    bl_label = "Add Cloth Sim"
    
    def execute(self, context):
        obj = context.active_object
        if obj is None:
            print("No valid object selected")
            
        else: 
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

class PHYSICS_OT_cloth_sims_clear(bpy.types.Operator):
    """Remove Cloth Sim"""
    bl_idname = "physics.clear_cloth_sims"
    bl_label = "Clear Cloth Sims"
    
    def execute(self, context):
        for obj in context.scene.objects:
            if obj.rigid_body:
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.modifier_remove(modifier="Cloth")
                
        return {'FINISHED'}
    
class PHYSICS_OT_collision_sims_clear(bpy.types.Operator):
    """Remove Collision"""
    bl_idname = "physics.clear_collision"
    bl_label = "Clear Collisions"

    def execute(self, context):
        for obj in context.scene.objects:
            if obj.rigid_body:
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.modifier_remove(modifier="Collision")
                
        return {'FINISHED'}

#-----------------------------------------------------------Rainbow Colour Textre--------------------------------------------------
class Material_OT_rainbow_colour_with_principled_bsdf(bpy.types.Operator):
    """Adds a Rainbow Color Ramp"""
    bl_idname = "material.rainbow_colour_with_principled_bsdf"
    bl_label = "Add Rainbow Color Ramp"

    def execute(self, context):
        # Get the active object
        obj = context.active_object
        if obj is None:
            self.report({'WARNING'}, "No active object found")
            return {'CANCELLED'}

        # Get or create the material
        material = obj.active_material
        if not material:
            material = bpy.data.materials.new(name="RainbowMaterial")
            obj.data.materials.append(material)

        # Enable 'Use Nodes'
        material.use_nodes = True

        # Check if the material has a node tree
        if not material.node_tree:
            self.report({'ERROR'}, "Failed to initialize node tree")
            return {'CANCELLED'}

        nodes = material.node_tree.nodes
        links = material.node_tree.links

            # Clear existing nodes
        nodes.clear()

        # Create a new Color Ramp Node
        color_ramp_node = nodes.new(type="ShaderNodeValToRGB")
        color_ramp_node.location = (-200, 0)

        # Create a Principled BSDF Node
        principled_node = nodes.new(type="ShaderNodeBsdfPrincipled")
        principled_node.location = (100, 0)

        # Link Color Ramp to Principled BSDF
        links.new(color_ramp_node.outputs['Color'], principled_node.inputs['Base Color'])

        # Configure the Color Ramp
        ramp = color_ramp_node.color_ramp 
        ramp.elements[0].color = (1, 0, 0, 1)  # Red
        ramp.elements[1].color = (1, 0.0349, 0.024, 1)  # Slightly shifted red
        ramp.elements[0].position = 0.0
        ramp.elements[1].position = 1.0
        ramp.color_mode = 'HSL'
        ramp.hue_interpolation = 'CCW'

        # Create an Output Material Node
        output_node = nodes.new(type="ShaderNodeOutputMaterial")
        output_node.location = (400, 0)

        # Link Principled BSDF to Output
        links.new(principled_node.outputs['BSDF'], output_node.inputs['Surface'])

        # Assign material to object if not already assigned
        if not obj.material_slots:
            bpy.ops.object.material_slot_add()
        obj.material_slots[0].material = material

        self.report({'INFO'}, f"Rainbow ramp added to {material.name}")
        return {'FINISHED'}
    
#---------------------------------------------------

class Material_OT_rainbow_colour(bpy.types.Operator):
    """Adds a Rainbow Color Ramp"""
    bl_idname = "material.rainbow"
    bl_label = "Add Rainbow Color Ramp"

    def execute(self, context):
        # Get the active object
        obj = context.active_object
        if obj is None:
            self.report({'WARNING'}, "No active object found")
            return {'CANCELLED'}

        # Get or create the material
        material = obj.active_material
        if not material:
            material = bpy.data.materials.new(name="RainbowMaterial")
            obj.data.materials.append(material)

        # Enable 'Use Nodes'
        material.use_nodes = True

        # Check if the material has a node tree
        if not material.node_tree:
            self.report({'ERROR'}, "Failed to initialize node tree")
            return {'CANCELLED'}

        nodes = material.node_tree.nodes
        links = material.node_tree.links

        # Create a new Color Ramp Node
        color_ramp_node = nodes.new(type="ShaderNodeValToRGB")
        color_ramp_node.location = (-200, 0)

        # Configure the Color Ramp
        ramp = color_ramp_node.color_ramp 
        ramp.elements[0].color = (1, 0, 0, 1)  # Red
        ramp.elements[1].color = (1, 0.0349, 0.024, 1)  # Slightly shifted red
        ramp.elements[0].position = 0.0
        ramp.elements[1].position = 1.0
        ramp.color_mode = 'HSL'
        ramp.hue_interpolation = 'CCW'

        # Assign material to object if not already assigned
        if not obj.material_slots:
            bpy.ops.object.material_slot_add()
        obj.material_slots[0].material = material

        self.report({'INFO'}, f"Rainbow ramp added to {material.name}")
        return {'FINISHED'}


#------------------------------------------------------- Registration ------------------------------------------------------------

classes = [
    VIEW3D_PT_Default_Setup_Addon,
    VIEW3D_PT_Render_Settings,
    VIEW3D_PT_Output_Settings,
    VIEW3D_PT_File_Sharing,
    VIEW3D_PT_Physics_Tab_Settings,
    VIEW3D_PT_Cloth_sims,
    VIEW3D_PT_Rigid_Bodies,
    VIEW3D_PT_Object_Constraints,
    VIEW3D_PT_Misc,
    VIEW3D_OT_toggle_overlays,
    
    RENDER_OT_cycle_gpu_button,
    RENDER_OT_change_resolution_1440p,
    RENDER_OT_change_resolution_1920x1080p,
    RENDER_OT_render_optimization,
    WORLD_OT_sky_texture_button,

    OUTPUT_OT_mp4_video_button,
    OUTPUT_OT_exr_video_button,

    EXTERNAL_DATA_OT_pack_resources,
    EXTERNAL_DATA_OT_relative_files,
    DATA_OT_purge_unused,
    
    PHYSICS_OT_passive_rigid_body,
    PHYSICS_OT_active_rigid_body,
    PHYSICS_OT_clear_rigid_body,

    CONSTRAINT_OT_add_track_to_constraint,
    CONSTRAINT_OT_remove_track_to_constraint,

    Material_OT_rainbow_colour_with_principled_bsdf,
    Material_OT_rainbow_colour,

    PHYSICS_OT_cloth_sims,
    PHYSICS_OT_cloth_sims_collision,
    PHYSICS_OT_cloth_sims_clear,
    PHYSICS_OT_collision_sims_clear,
    
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()