import bpy

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