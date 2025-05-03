import bpy 

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
    