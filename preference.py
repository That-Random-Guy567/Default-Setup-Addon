import bpy
from bpy.props import BoolProperty, FloatProperty, IntProperty, StringProperty, EnumProperty

class Default_Setup_Addon_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    example_bool: BoolProperty( #type: ignore
        name="Enable Feature",
        description="Enable or disable a specific feature",
        default=True,
    )

    example_int: IntProperty( #type: ignore
        name="Example Integer",
        description="An integer value for customization",
        default=10,
        min=1,
        max=100,
    )

    example_float: FloatProperty( #type: ignore
        name="Example Float",
        description="A float value for customization",
        default=0.5,
        min=0.0,
        max=1.0,
    )

    example_string: StringProperty( #type: ignore
        name="Example Text",
        description="A text field for user input",
        default="Default Text",
    )

    example_enum: EnumProperty( #type: ignore
        name="Example Dropdown",
        description="Choose an option from the dropdown",
        items=[
            ('OPTION_A', "Option A", "Description for Option A"),
            ('OPTION_B', "Option B", "Description for Option B"),
            ('OPTION_C', "Option C", "Description for Option C"),
        ],
        default='OPTION_A',
    )

    def draw(self, context):
        
        # Draw the preferences UI
        layout = self.layout

        layout.label(text="Customize your Addon Preferences:")

        box = layout.box()
        box.label(text="Main Settings")
        box.prop(self, "example_bool")
        box.prop(self, "example_enum")  
               
        box2 = layout.box()
        box2.label(text="Advanced Settings")
        box2.prop(self, "example_int")
        box2.prop(self, "example_float")
        box2.prop(self, "example_string")