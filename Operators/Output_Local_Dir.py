import bpy
import os

class OUTPUT_OT_local_dir(bpy.types.Operator):
    """Set the output directory for rendering to local 'frames' folder"""
    bl_idname = "output.local_dir"
    bl_label = "Set Output Directory"
    bl_options = {'REGISTER', 'UNDO'}

    def create_frames_dir(self, base_path):
        """Create frames directory if it doesn't exist"""
        frames_dir = os.path.join(base_path, "Frames")
        if not os.path.exists(frames_dir):
            os.makedirs(frames_dir)
        return frames_dir

    def execute(self, context):
        # Get the current blend file's directory
        blend_file_dir = bpy.path.abspath("//")
        
        if not blend_file_dir:
            self.report({'ERROR'}, "Please save your file first!")
            return {'CANCELLED'}
        
        # Create and set path to frames subdirectory
        frames_path = self.create_frames_dir(blend_file_dir)
        
        # Set the output directory and format
        context.scene.render.filepath = os.path.join(frames_path, "frame_")
        
        self.report({'INFO'}, f"Output directory set to: {frames_path}")
        return {'FINISHED'}