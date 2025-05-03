import bpy 

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

        self.log({'INFO'}, "Nishita sky texture applied!")
        return {'FINISHED'}