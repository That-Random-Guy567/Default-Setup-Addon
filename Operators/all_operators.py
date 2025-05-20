import bpy

# ---------------- Render Settings ----------------
from .Render_GPU_btn import RENDER_OT_cycle_gpu_button
from .Render_Optimize_Cycles import RENDER_OT_render_optimization
from .World_SkyTex_Btn import WORLD_OT_sky_texture_button

# ---------------- Output Settings ----------------
from .Render_Resolution_1080p import RENDER_OT_change_resolution_1080x1920p
from .Render_Resolution_1440p import RENDER_OT_change_resolution_1440p
from .Output_Exr_Btn import OUTPUT_OT_exr_video_button
from .Output_Mp4_Btn import OUTPUT_OT_mp4_video_button
from .Output_Local_Dir import OUTPUT_OT_local_dir

# ---------------- File Sharing ----------------
from .Data_Purge_Unused import DATA_OT_purge_unused
from .External_Data_Pack import EXTERNAL_DATA_OT_pack_resources
from .External_Data_Relative import EXTERNAL_DATA_OT_relative_files

# ---------------- Physics Tools ----------------
# cloth simulation
from .Phyx_Active_Rigid import PHYSICS_OT_active_rigid_body
from .Phyx_Clear_Rigid import PHYSICS_OT_clear_rigid_body
from .Phyx_Passive_Rigid import PHYSICS_OT_passive_rigid_body

# rigid body simulation
from .Phyx_Cloth_Collision import PHYSICS_OT_cloth_sims_collision
from .Phyx_Cloth_Collision_Clear import PHYSICS_OT_collision_sims_clear
from .Phyx_Cloth_Sim import PHYSICS_OT_cloth_sims
from .Phyx_Cloth_Sim_Clear import PHYSICS_OT_cloth_sims_clear

# ---------------- Constraint Tools ----------------
from .Constraint_Track import CONSTRAINT_OT_add_track_to_constraint
from .Constraint_Track_Remove import CONSTRAINT_OT_remove_track_to_constraint

# ---------------- Misc Functions ----------------
from .Material_Rainbow_BSDF import Material_OT_rainbow_colour_with_principled_bsdf
from .Material_Rainbow_Color_Ramp import Material_OT_rainbow_colour
from .Toggle_Overlays import VIEW3D_OT_toggle_overlays

# List of all operators for easy registration
all_operators = [
    # Render
    RENDER_OT_cycle_gpu_button,
    RENDER_OT_render_optimization,

    # Output
    RENDER_OT_change_resolution_1080x1920p,
    RENDER_OT_change_resolution_1440p,
    OUTPUT_OT_exr_video_button,
    OUTPUT_OT_mp4_video_button,
    OUTPUT_OT_local_dir,

    # File Sharing
    DATA_OT_purge_unused,
    EXTERNAL_DATA_OT_pack_resources,
    EXTERNAL_DATA_OT_relative_files,

    # Physics
    PHYSICS_OT_active_rigid_body,
    PHYSICS_OT_clear_rigid_body,
    PHYSICS_OT_passive_rigid_body,
    PHYSICS_OT_cloth_sims_collision,
    PHYSICS_OT_collision_sims_clear,
    PHYSICS_OT_cloth_sims,
    PHYSICS_OT_cloth_sims_clear,

    # Constraints
    CONSTRAINT_OT_add_track_to_constraint,
    CONSTRAINT_OT_remove_track_to_constraint,

    # Materials
    Material_OT_rainbow_colour_with_principled_bsdf,
    Material_OT_rainbow_colour,

    # World
    WORLD_OT_sky_texture_button,

    # Misc
    VIEW3D_OT_toggle_overlays,
]